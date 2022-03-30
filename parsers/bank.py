from abc import ABC, abstractmethod


class IBankParser(ABC):

    @abstractmethod
    def get_currency_rate(self):
        pass