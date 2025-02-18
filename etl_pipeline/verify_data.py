from sqlmodel import Session, select, create_engine
from load import Movie, Genre, MovieGenre

def display_data():
    engine = create_engine("sqlite:///movies.db")
    with Session(engine) as session:
        movies = session.exec(select(Movie)).all()
        genres = session.exec(select(Genre)).all()
        movie_genres = session.exec(select(MovieGenre)).all()

        print("Movies:")
        for movie in movies:
            print(movie)
        
        print("\nGenres:")
        for genre in genres:
            print(genre)
        
        print("\nMovieGenres:")
        for movie_genre in movie_genres:
            print(movie_genre)

if __name__ == "__main__":
    display_data()
    
    