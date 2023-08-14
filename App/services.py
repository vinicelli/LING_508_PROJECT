from App.Classes import *
from db.mysql_repository import MysqlRepository
from Test.example_reviews import *
test_restaurant = MenuQuery(
                            id=1,
                            restaurant_name="Fantani's",
                            item_query='pizza')



class Services:
    def __init__(self):
        self.repo = MysqlRepository()

    def add_to_reviews(self, menu_item_name):
        restaurant_id = self.repo.get_restaurant_id(MenuQuery(id=1, restaurant_name="Fantani's", item_query=menu_item_name))

        for review in test_reviews:
            if menu_item_name.lower() in review.review_text.lower():
                review.restaurant_id = restaurant_id
                self.repo.insert_review(review)

    def get_all_reviews(self):
        return self.repo.get_all_reviews()

    def clear_all_reviews(self):
        self.repo.clear_all_reviews()

