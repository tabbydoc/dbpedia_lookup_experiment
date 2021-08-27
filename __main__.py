import config
from config import logger
from experiment_logger import journal
from lookup_service import service
from parameters_experiment import LookupServiceParametersExperiment
from parameters_experiment import T2Dv2Processor

# =====================
# Начало работы скрипта
# =====================
#
# Создаём модель эксперимента
experiment = LookupServiceParametersExperiment(config.PATH_TO_TABLES,
                                               T2Dv2Processor(),
                                               service,
                                               journal, max_results=[10, 20])

logger.info(config.GREETINGS_MSG, type(experiment).__name__, config.URL, config.PATH_TO_TABLES, config.query_args)

# Начинаем эксперимент
experiment.run()
