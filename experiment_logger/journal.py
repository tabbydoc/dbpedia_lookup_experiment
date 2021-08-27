class Metric:
    """
    Класс, описывающий метрику для подсчёта результатов эксперимента
    """
    name: str

    def check(self, entity, results):
        pass

    def total(self, values):
        pass


class Journal:
    """
    Журнал для хранения результатов эксперимента
    """
    metrics: list

    def __init__(self, path):
        self.entries = dict()
        self.score_table = dict()
        self.path = path

    def new_entry(self, filename, key, value, results):
        pass

    def _create_metric_dict(self, value, results):
        return {metric.name: metric.check(entity=value, results=results) for metric in self.metrics}

    def save(self):
        pass
