# etl_pipeline/load.py
from sqlmodel import SQLModel, create_engine, Session, Field, select, delete
from typing import List, Optional
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    release_year: str
    release_date: Optional[str]
    days_since_release: Optional[str]
    months_since_release: Optional[str]
    years_since_release: Optional[str]
    director: str
    synopsis: str

class Genre(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class MovieGenre(SQLModel, table=True):
    movie_id: int = Field(foreign_key="movie.id", primary_key=True)
    genre_id: int = Field(foreign_key="genre.id", primary_key=True)

def create_db_and_tables():
    engine = create_engine("sqlite:///movies.db")
    SQLModel.metadata.create_all(engine)
    logger.info('Banco de dados e tabelas criados com sucesso.')

def load_data(movie_data, genres):
    engine = create_engine("sqlite:///movies.db")
    try:
        with Session(engine) as session:
            movie = Movie(**movie_data)
            session.add(movie)
            session.commit()
            session.refresh(movie)
            
            for genre_name in genres:
                genre = session.query(Genre).filter(Genre.name == genre_name).first()
                if not genre:
                    genre = Genre(name=genre_name)
                    session.add(genre)
                    session.commit()
                    session.refresh(genre)
                movie_genre = MovieGenre(movie_id=movie.id, genre_id=genre.id)
                session.add(movie_genre)
            
            session.commit()
        logger.info(f'Dados carregados com sucesso para o filme "{movie_data['title']}"')
    except Exception as e:
        logger.error(f'Erro ao carregar dados no banco de dados: {e}')

# limpando o banco de dados

def clear_db():
    engine = create_engine('sqlite:///movies.db')
    try:
        with Session(engine) as session:
            session.exec(delete(Movie))
            session.exec(delete(Genre))
            session.exec(delete(MovieGenre))
            session.commit()
        logger.info('Banco de dados limpo com sucesso.')
    except Exception as e:
        logger.error(f'Erro ao limpar banco de dados: {e}')

if __name__ == "__main__":
    clear_db()