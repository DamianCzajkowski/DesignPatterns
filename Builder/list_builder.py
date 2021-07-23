import csv
from .builder import Builder


class ListBuilder(Builder):

    __data = None

    def set_data(self, data):
        self.__data = data

    def save_data(self):
        with open('some_data.csv', 'w', newline="") as file:
            writer = csv.writer(file, delimiter=",")
            for row in self.__data:
                writer.writerow(row)
