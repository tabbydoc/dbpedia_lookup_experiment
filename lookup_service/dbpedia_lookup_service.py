import json

import requests

import config
from .service import LookupService


class DBpediaQueryService(LookupService):
    """
    Класс для работы с DBpedia Lookup
    """

    def execute_query(self, query):
        """
        Непосредственно выполняет запрос к DBpedia Lookup

        Args:
            query: строка, для которой нужно выполнить запрос
        Returns:
            list: список URI ссылок на сущности из DBpedia
        """
        self.args['query'] = query  # К имеющимся параметрам добавляем текст запроса
        response = requests.get(url=config.URL, params=self.args)

        if response.status_code == 200:
            # Создаём список URI ссылок из полученного JSON ответа
            json_response = json.loads(response.text)
            return [doc['resource'][0] for doc in json_response['docs']]
        else:
            raise requests.exceptions.ConnectionError(response.reason)
