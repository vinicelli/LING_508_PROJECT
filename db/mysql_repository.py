from db.repository import Repository
from App.Classes import MenuQuery, Review
import mysql.connector

class MysqlRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': '32000',  # to run LOCALLY, this should be 32000
            'database': 'reviews'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def create_tables(self):
        create_restaurants_table = """
            CREATE TABLE IF NOT EXISTS restaurants (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_name VARCHAR(255),
                item_query VARCHAR(255)
            )
        """

        create_reviews_table = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_id INT,
                author VARCHAR(255),
                rating FLOAT,
                review_text TEXT,
                sentiment_score FLOAT,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
            )
        """

        self.cursor.execute(create_restaurants_table)
        self.cursor.execute(create_reviews_table)
        self.connection.commit()

    def insert_restaurant(self, menu_item: MenuQuery):
        sql = 'INSERT INTO restaurants (restaurant_name, item_query) VALUES (%s, %s)'
        values = (menu_item.restaurant_name, menu_item.item_query)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def insert_review(self, review: Review):
        sql = 'INSERT INTO reviews (restaurant_id, author, rating, review_text, sentiment_score) ' \
              'VALUES (%s, %s, %s, %s, %s)'
        values = (review.restaurant_id, review.author, review.rating, review.review_text, review.sentiment_score)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def get_restaurant_id(self, menu_item: MenuQuery) -> int:
        sql = 'SELECT id FROM restaurants WHERE restaurant_name = %s AND item_query = %s'
        values = (menu_item.restaurant_name, menu_item.item_query)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            # If the restaurant does not exist in the database, insert it and get its ID
            self.insert_restaurant(menu_item)
            return self.cursor.lastrowid
