from abc import ABC, abstractmethod
from App.Classes import MenuItem, Review

class Repository(ABC):

    @abstractmethod
    def insert_restaurant(self, menu_item: MenuItem) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert_review(self, review: Review) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_restaurant_id(self, menu_item: MenuItem) -> int:
        raise NotImplementedError
