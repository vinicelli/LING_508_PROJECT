from db.repository import Repository
import mysql.connector
from Test.example_reviews import *

class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',  # to run LOCALLY, this should be localhost
            'port': '3306',  # to run LOCALLY, this should be 32000
            'database': 'reviews'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

        self.create_tables()
        self.insert_restaurant(test_restaurant)
        self.initial_reviews(test_reviews_list)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def create_tables(self):
        create_restaurants_table = """
            CREATE TABLE IF NOT EXISTS restaurants (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_name VARCHAR(255) NOT NULL
            )
        """

        create_reviews_table = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_id INT NOT NULL,
                author VARCHAR(255) NOT NULL,
                rating FLOAT NOT NULL,
                review_text TEXT NOT NULL,
                sentiment_score FLOAT NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        """

        self.cursor.execute(create_restaurants_table)
        self.cursor.execute(create_reviews_table)
        self.connection.commit()

    def initial_reviews(self, reviews_list):
        restaurant_id = test_restaurant.id
        reviews = Review.list_to_reviews(reviews_list, restaurant_id)
        for review in reviews:
            self.insert_review(review)

    def insert_restaurant(self, restaurant: Restaurant):
        sql = 'SELECT COUNT(*) FROM restaurants WHERE restaurant_name = %s'
        values = (restaurant.restaurant_name,)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if result[0] > 0:
            return

        sql = 'INSERT INTO restaurants (restaurant_name) VALUES (%s)'
        values = (restaurant.restaurant_name,)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def get_restaurant_id_by_name(self, restaurant_name):
        sql = 'SELECT id FROM restaurants WHERE restaurant_name = %s'
        values = (restaurant_name,)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def insert_review(self, review: Review):
        sql = 'INSERT INTO reviews (restaurant_id, author, rating, review_text, sentiment_score) ' \
              'VALUES (%s, %s, %s, %s, %s)'
        values = (review.restaurant_id, review.author, review.rating, review.review_text, review.sentiment_score)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def get_all_reviews(self):
        sql = 'SELECT * FROM reviews'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        reviews = []
        for row in rows:
            review = Review(
                id=row[0],
                restaurant_id=row[1],
                author=row[2],
                rating=row[3],
                review_text=row[4],
                sentiment_score=row[5]
            )
            reviews.append(review)
        return reviews

    def get_reviews_by_restaurant(self, restaurant_name):
        # Get the restaurant ID first
        sql = 'SELECT id FROM restaurants WHERE restaurant_name = %s'
        values = (restaurant_name,)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if not result:
            return []
        restaurant_id = result[0]

        second_cursor = self.connection.cursor()
        sql = 'SELECT * FROM reviews WHERE restaurant_id = %s'
        values = (restaurant_id,)
        second_cursor.execute(sql, values)
        rows = second_cursor.fetchall()
        second_cursor.close()

        reviews = []
        for row in rows:
            review = Review(
                id=row[0],
                restaurant_id=row[1],
                author=row[2],
                rating=row[3],
                review_text=row[4],
                sentiment_score=row[5]
            )
            reviews.append(review)
        return reviews

    def get_all_restaurants(self):
        sql = 'SELECT restaurant_name FROM restaurants'
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        restaurants = [row[0] for row in rows]
        return restaurants

    def clear_all_reviews(self):
        sql = 'DELETE FROM reviews'
        self.cursor.execute(sql)
        self.connection.commit()

    def clear_all_restaurants(self):
        sql = 'DELETE FROM restaurants'
        self.cursor.execute(sql)
        self.connection.commit()
