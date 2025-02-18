# etl_pipeline/main.py
from extract import fetch_movie_data
from transform import transform_data
from load import create_db_and_tables, load_data
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline(movie_title):
    try:
        create_db_and_tables()
        movie_data = fetch_movie_data(movie_title)
        if movie_data:
            transformed_data = transform_data(movie_data)
            if transform_data:
                genres = transformed_data.pop("genres")
                load_data(transformed_data, genres)
            else:
                logger.error("A transformação de dados falhou")
        else:
            logger.error('A extração de dados falhou')
    except Exception as e:
        logger.error(f'Erro no pipeline ETL: {e}')

if __name__ == "__main__":
    movie_title = "Ironman"
    run_pipeline(movie_title)
    
    