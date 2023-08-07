from App.Classes import *
from db.mysql_repository import MysqlRepository
test_restaurant = MenuQuery(
                            id=1,
                            restaurant_name="fantani's",
                            item_query='pizza')

test_reviews = [
    Review(
        restaurant_id=2,
        author="Foodie456",
        rating=5.0,
        review_text="The Grilled Chicken Sandwich was delicious and juicy!",
        sentiment_score=0.95,
    ),
    Review(
        restaurant_id=2,
        author="Foodie789",
        rating=4.0,
        review_text="The French Fries were crispy and perfectly seasoned.",
        sentiment_score=0.85,
    ),
    Review(
        restaurant_id=2,
        author="HealthyEater",
        rating=4.5,
        review_text="The Caesar Salad was fresh and had a great dressing.",
        sentiment_score=0.88,
    ),
    Review(
        restaurant_id=1,
        author="PizzaLover",
        rating=4.2,
        review_text="The Margherita Pizza was amazing! Perfectly baked with fresh ingredients.",
        sentiment_score=0.91,
    ),
    Review(
        restaurant_id=1,
        author="Foodie333",
        rating=3.8,
        review_text="The restaurant has a wide variety of options, but I didn't try the pizza.",
        sentiment_score=0.75,
    ),
    Review(
        restaurant_id=3,
        author="PizzaFan",
        rating=4.9,
        review_text="The BBQ Chicken Pizza was the highlight of my meal! Highly recommended.",
        sentiment_score=0.96,
    ),
    Review(
        restaurant_id=4,
        author="HealthyChoice",
        rating=4.5,
        review_text="The Veggie Wrap was delicious and filling, a great option alongside pizza.",
        sentiment_score=0.88,
    ),
]


class Services:
    def __init__(self):
        self.repo = MysqlRepository()

    def add_to_reviews(self, menu_item_name):
        restaurant_id = self.repo.get_restaurant_id(MenuQuery(id=1, restaurant_name="fantani's", item_query=menu_item_name))

        for review in test_reviews:
            if menu_item_name.lower() in review.review_text.lower():
                review.restaurant_id = restaurant_id
                self.repo.insert_review(review)


services = Services()
services.add_to_reviews('pizza')