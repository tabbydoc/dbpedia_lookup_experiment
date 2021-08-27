import os

from requests import exceptions

from config import logger
from experiment_logger.journal import Journal
from lookup_service.service import LookupService


class TableProcessor:
    """
    Класс-обработчик файла таблицы
    """

    def __init__(self):
        pass

    def process(self, table_name):
        """
        Возвращает для файла table_name словарь {key : URI}
        :param table_name: путь до файла
        :return: dict, построенного по типу {key: URI}
        """
        return {}


class Experiment:
    """
    Класс, описывающий эксперимент для набора данных
    """

    def __init__(self,
                 path_to_tables: str,
                 table_processor: TableProcessor,
                 lookup_service: LookupService,
                 experiment_logger: Journal,
                 **params):
        """
        Конструктор эксперимента

        Args:
            path_to_tables: путь до файлов набора данных
            table_processor: класс-обработчик файла с таблицей
            lookup_service: класс для обращения к Lookup сервису
            experiment_logger: журнал для записи результатов эксперимента
            params: параметры эксперимента (используются в каждом эксперименте по-разному)
        """

        self.path_to_tables = path_to_tables
        self.files = os.listdir(path_to_tables)
        self.table_processor = table_processor
        self.service = lookup_service
        self.journal = experiment_logger
        self.params = params

    def run(self):
        """
        Начало эксперимента
        """
        self.start()
        self.finish()

    def start(self):
        """
        Действия при запуске эксперимента.

        В этой реализации для каждой таблицы из набора данных получаем сущности,
        делаем запрос к Lookup сервису и делаем запись в журнал эксперимента
        """

        total_tables = len(self.files)
        success_tables = 0

        for counter, filename in enumerate(self.files, 1):
            # Получаем словарь сущностей
            entities = self.table_processor.process(os.path.join(self.path_to_tables, filename))

            try:
                for key, entity in entities.items():
                    # Выполняем запрос к Lookup сервису
                    results = self.service.execute_query(query=key)
                    # Делаем запись в журнале эксперимента
                    self.journal.new_entry(filename=filename, key=key, value=entity, results=results)
            except exceptions.ConnectionError as e:
                # Ловим исключение при плохом соединении с сервисом
                logger.warning('Table %s is skipped because of connection troubles:\n\t%s', filename, e)
            else:
                percent = counter / total_tables * 100
                logger.info('%d / %d (%0.1f %%) %s',
                            counter, total_tables, percent, filename)
                success_tables += 1

        logger.info('Total tables: %d, successfully processed tables: %d', total_tables, success_tables)

    def finish(self):
        """
        Действия при окончании эксперимента
        """
        self.journal.save()
