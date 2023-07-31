import unittest
import mysql.connector
from App.Classes import RestaurantReviewDatabase, Review, RestaurantQuery

class TestRestaurantReviewDatabase(unittest.TestCase):
    def setUp(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'reviews',
        }

        self.test_db_connection = mysql.connector.connect(**config)
        self.test_cursor = self.test_db_connection.cursor()


    def test_insert_restaurant_query(self):
        database = RestaurantReviewDatabase()

        query = "Italian Food"
        restaurant_name = "Pasta Paradise"
        restaurant = database.insert_restaurant_query(query, restaurant_name)

        query = "SELECT * FROM restaurants WHERE restaurant_name = %s"
        self.test_cursor.execute(query, (restaurant_name,))
        result = self.test_cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], query)

    def test_insert_reviews(self):
        database = RestaurantReviewDatabase()

        query = "Italian Food"
        restaurant_name = "Pasta Paradise"
        restaurant = database.insert_restaurant_query(query, restaurant_name)

        review_text = "The pasta was delicious!"
        rating = 4.5
        sentiment_score = 0.9
        review = Review(restaurant, review_text, rating, sentiment_score)

        database.insert_reviews([review], restaurant)

        query = "SELECT * FROM reviews WHERE restaurant_id = %s"
        self.test_cursor.execute(query, (restaurant.id,))
        result = self.test_cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[3], review_text)

    def tearDown(self):
        self.test_cursor.close()
        self.test_db_connection.close()

if __name__ == "__main__":
    unittest.main()