from abc import ABC, abstractmethod
from App.Classes import MenuQuery, Review

class Repository(ABC):

    @abstractmethod
    def insert_restaurant(self, menu_item: MenuQuery) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert_review(self, review: Review) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_restaurant_id(self, menu_item: MenuQuery) -> int:
        raise NotImplementedError
