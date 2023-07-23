from App.Classes import *

def test_menu_item_creation():
    menu_item = MenuItem("Burger")
    assert menu_item.name == "Burger"


def test_review_creation():
    menu_item = MenuItem("Pizza")
    review = Review(menu_item, "The pizza was delicious!", 0.8)

    assert review.menu_item == menu_item
    assert review.review_text == "The pizza was delicious!"
    assert review.sentiment_score == 0.8

