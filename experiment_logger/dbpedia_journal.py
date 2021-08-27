import os

import pandas as pd

from .journal import Journal
from .journal import Metric


class ContainedInResultsMetric(Metric):
    name = 'annotated_entity_score'

    def check(self, entity, results):
        if entity in results:
            return 1
        else:
            return 0

    def total(self, values):
        return sum(values) / len(values)


class DBpediaJournal(Journal):
    metrics = [ContainedInResultsMetric()]

    def __init__(self, path):
        super().__init__(path)
        self.sheet_name_suffix = ''

    def new_entry(self, filename, key, value, results):
        if filename in self.entries:
            keys = self.entries[filename]

            if key not in keys:
                keys[key] = self._create_metric_dict(value, results)
            else:
                return
        else:
            self.entries[filename] = {
                key: self._create_metric_dict(value, results)
            }

    def set_sheet_suffix(self, suffix):
        self.sheet_name_suffix = suffix

    def save(self):
        for metric in self.metrics:
            self.score_table[metric.name] = []
            for _, metric_scores in self.entries.items():
                metric_values = [v[metric.name] for _, v in metric_scores.items()]
                self.score_table[metric.name].append(metric.total(metric_values))

        total_data = pd.DataFrame(self.score_table, index=self.entries.keys())

        try:
            with pd.ExcelWriter(path=os.path.join(self.path, f'results.xlsx'), mode='a') as writer:
                total_data.to_excel(writer, sheet_name=f'result_{self.sheet_name_suffix}')
        except FileNotFoundError as e:
            with pd.ExcelWriter(path=os.path.join(self.path, f'results.xlsx'), mode='w') as writer:
                total_data.to_excel(writer, sheet_name=f'result_{self.sheet_name_suffix}')
