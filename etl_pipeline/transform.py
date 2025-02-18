from datetime import datetime
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def transform_data(movie_data):
    try:
        transformed_data = {
            'title': movie_data.get('Title'),
            'release_year': movie_data.get('Year'),
            'release_date': datetime.strptime(movie_data.get('Released'), "%d %b %Y").date().isoformat() if movie_data.get('released') else None,
            'director': movie_data.get('Director'),
            'synopsis': movie_data.get('Plot'),
            'genres': movie_data.get('Genre').split(", ") if movie_data.get('Genre') else []
        }

        # Calcular a quantidade de dias, meses e anos que o filme foi lançado
        if transformed_data['release_date']:
            release_date = datetime.strptime(transformed_data['release_date'], "%Y-%m-%d")
            current_date = datetime.now()
            delta = current_date - release_date
            transformed_data['days_since_release'] = delta.days
            transformed_data['months_since_release'] = delta.days // 30
            transformed_data['years_since_release'] = delta.days // 365

        logger.info(f"Dados transformados com sucesso para o filme '{transformed_data['title']}'")
        return transformed_data
    except Exception as e:
        logger.error(f'Erro ao transformar dados: {e}')
        return None
