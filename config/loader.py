import logging.config
import os

import yaml

with open(os.path.join(os.path.dirname(__file__), 'config.yaml')) as conf:
    # Загружаем конфиг скрипта
    params = yaml.safe_load(conf)

with open((os.path.join(os.path.dirname(__file__), 'logger_config.yaml'))) as log_conf:
    # Загружаем конфиг лога
    config = yaml.safe_load(log_conf)
    logging.config.dictConfig(config)
