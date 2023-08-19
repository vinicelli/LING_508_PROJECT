from db.mysql_repository import MysqlRepository
from App.Classes import Restaurant, Review
import unittest

class TestMysqlRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This method is called once at the beginning of the test suite.
        cls.repo = MysqlRepository()

    def setUp(self):

        self.repo.clear_all_data()

    def test_restaurant_and_reviews(self):
        restaurant = MenuQuery("Bistro Cafe", "coffee")
        restaurant_id = self.repo.get_restaurant_id(restaurant)

        self.assertIsNotNone(restaurant_id)

        review1 = Review(restaurant_id, "John", 4.5, "Great coffee!", 0.8)
        review2 = Review(restaurant_id, "Jane", 3.0, "Good place, but a bit noisy.", 0.5)

        self.repo.insert_review(review1)
        self.repo.insert_review(review2)

        # Searching for a keyword in a review
        self.assertTrue(review1.search_review_text("coffee"))
        self.assertFalse(review2.search_review_text("excellent"))

    def test_empty_reviews(self):
        # Test when no reviews are available for a restaurant.
        restaurant = MenuQuery("Nonexistent Restaurant", "cuisine")
        restaurant_id = self.repo.get_restaurant_id(restaurant)

        self.assertIsNone(restaurant_id)  # Make sure restaurant ID is not found

    # Add more test cases to cover other aspects of your code, like edge cases, exceptions, etc.

if __name__ == '__main__':
    unittest.main()
