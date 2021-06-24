from csv import DictWriter
from .list_builder import ListBuilder
from .my_list_builder import MylistBuilder
from .dict_builder import DictBuilder


class Director:
    def __init__(self) -> None:
        self.builder = None
        self.data = None

    def set_data(self, data):
        comma_exists = False
        self.data = data
        if isinstance(self.data[0], dict):
            self.builder = DictBuilder()
            return
        for row in data:
            for item in row:
                item_str = str(item)
                if ',' in item_str:
                    comma_exists = True
        self.builder = MylistBuilder() if not comma_exists else ListBuilder()

    def set_builder(self, builder):
        self.builder = builder

    def create_csv(self):
        self.builder.set_data(self.data)
        self.builder.save_data()
