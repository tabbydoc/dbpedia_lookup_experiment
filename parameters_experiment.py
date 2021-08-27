import pandas as pd

import config
from config import logger
from experiment_logger.dbpedia_journal import DBpediaJournal
from lookupXP import Experiment
from lookupXP import TableProcessor


class T2Dv2Processor(TableProcessor):
    """
    Класс-обработчик файла таблицы из набора данных T2Dv2
    """

    def process(self, table_name):
        table = pd.read_csv(table_name, sep=',', usecols=[0, 1], names=['URI', 'key'])
        return dict(zip(table['key'], table['URI']))


class LookupServiceParametersExperiment(Experiment):
    """
    Эксперимент с различными параметрами lookup сервиса
    """
    journal: DBpediaJournal

    def run(self):
        max_results = self.params['max_results']

        for value in max_results:
            logger.info('Starting experiment with maxResults = %d', value)
            self.journal.set_sheet_suffix(value)
            config.query_args['maxResults'] = value
            super().start()
            super().finish()
