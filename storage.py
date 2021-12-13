import csv
import json


class Storage:
    def __init__(self, name='vk.csv', _type='csv', data=[]):
        self.data = data
        self.name = name
        self.type = _type
        self.names = [
            "first_name", "last_name",
            "country", "city",
            "bdate", "sex"
        ]
        self.types = {
            'csv': self.store_csv,
            'json': self.store_json,
            'tsv': self.store_tsv
        }

    def store_friends(self):
        if len(self.data) > 1:
            if self.types.get(self.type):
                func = self.types.get(self.type)
                func()
            else:
                print('ОШИБКА!!! неизвестный формат записи')

    def store_csv(self):
        with open(self.name, mode="w", encoding='utf-8') as w_file:
            file_writer = csv.DictWriter(w_file, delimiter=",",
                                         lineterminator="\r", fieldnames=self.names)
            file_writer.writeheader()
            for i in self.data:
                file_writer.writerow(i)
        pass

    def store_json(self):
        with open(self.name, 'w') as outfile:
            json.dump(self.data, outfile)

    def store_tsv(self):
        with open(self.name, 'wt', encoding='utf-8') as file:
            tsv_writer = csv.writer(file, delimiter='\t')
            for i in self.data:
                tsv_writer.writerow(list(i.values()))
