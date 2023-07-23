from App.Classes import *

def test_menu_item_creation(self):
    menu_item = MenuItem("Burger")
    self.assertEqual(menu_item.name, "Burger")


def test_review_creation(self):
    menu_item = MenuItem("Pizza")
    review = Review(menu_item, "The pizza was delicious!", 0.8)

    self.assertEqual(review.menu_item, menu_item)
    self.assertEqual(review.review_text, "The pizza was delicious!")
    self.assertEqual(review.sentiment_score, 0.8)
