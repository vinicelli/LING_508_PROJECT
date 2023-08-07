from db.mysql_repository import *
from App.Classes import MenuQuery
import unittest


class TestMysqlRepository(unittest.TestCase):

    def test_restaurant_and_reviews(self):
        repo = MysqlRepository()

        restaurant = MenuQuery("Bistro Cafe", "coffee")
        restaurant_id = repo.get_restaurant_id(restaurant)

        self.assertIsNotNone(restaurant_id)

        review1 = Review(restaurant_id, "John", 4.5, "Great coffee!", 0.8)
        review2 = Review(restaurant_id, "Jane", 3.0, "Good place, but a bit noisy.", 0.5)

        repo.insert_review(review1)
        repo.insert_review(review2)

        # Searching for a keyword in a review
        self.assertTrue(review1.search_review_text("coffee"))
        self.assertFalse(review2.search_review_text("excellent"))



if __name__ == '__main__':
    unittest.main()
