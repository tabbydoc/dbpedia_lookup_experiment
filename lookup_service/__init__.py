import config
from .dbpedia_lookup_service import DBpediaQueryService

# Определяем lookup, с которым будет работать скрипт
service = DBpediaQueryService(config.query_args)
