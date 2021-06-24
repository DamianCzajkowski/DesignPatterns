from abc import ABC, abstractmethod


class Builder(ABC):

    __data = None

    @abstractmethod
    def set_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
