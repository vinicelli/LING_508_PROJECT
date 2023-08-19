from App.Classes import *
from db.mysql_repository import MysqlRepository
from Test.example_reviews import *


class Services:
    def __init__(self):
        self.repo = MysqlRepository()

    def add_restaurant(self, restaurant_name):
        restaurant = Restaurant(restaurant_name=restaurant_name)
        self.repo.insert_restaurant(restaurant)

    def add_review(self, review: Review):
        self.repo.insert_review(review)

    def get_all_reviews(self):
        return self.repo.get_all_reviews()

    def get_reviews_by_restaurant(self, restaurant_name):
        return self.repo.get_reviews_by_restaurant(restaurant_name)

    def get_all_restaurants(self):
        return self.repo.get_all_restaurants()

    def clear_all_reviews(self):
        self.repo.clear_all_reviews()

    def clear_all_restaurants(self):
        self.repo.clear_all_restaurants()

    def get_restaurant_id_by_name(self, restaurant_name):
        return self.repo.get_restaurant_id_by_name(restaurant_name)



