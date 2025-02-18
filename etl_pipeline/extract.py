import requests
import os
import logging

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = 'http://www.omdbapi.com/?i=tt3896198&apikey=a1412414'

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_movie_data(title):
    try:     
        params = {
            't': title,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestsExceptions as e:
        logger.error(f"Erro ao extrair dados do filme '{title}': {e}")
        return None