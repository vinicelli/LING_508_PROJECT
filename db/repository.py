from abc import ABC, abstractmethod
from App.Classes import Restaurant, Review

class Repository(ABC):

    @abstractmethod
    def insert_restaurant(self, menu_item: Restaurant) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert_review(self, review: Restaurant) -> None:
        raise NotImplementedError

