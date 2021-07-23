import csv
from .builder import Builder


class DictBuilder(Builder):

    __data = None

    def set_data(self, data):
        self.__data = data

    def save_data(self):
        with open('some_dict_data.csv', 'w', newline="", encoding='UTF-8') as file:
            keys = self.__data[0].keys()
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.__data)
