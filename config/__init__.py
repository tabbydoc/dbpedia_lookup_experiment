import logging.config
from urllib.parse import urljoin

from .loader import params

# Параметры скрипта
PATH_TO_TABLES = params['path_to_tables']
PATH_TO_SAVE = params['path_to_save']
URL = urljoin(f"{params['dbpedia']['host']}:{params['dbpedia']['port']}", params['dbpedia']['api_path'])
query_args = params['dbpedia']['query_args']

# Параметры лога
logger = logging.getLogger('mainLogger')
GREETINGS_MSG = 'Starting experiment %s\n\tLookup Service URL: %s\n\tPath to tables: %s\n\tQuery arguments: %s\n'
