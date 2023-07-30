import mysql.connector


class RestaurantQuery:
    def __init__(self, query, restaurant_name):
        self.query = query
        self.restaurant_name = restaurant_name

    def __str__(self):
        return self.query

    def insert_into_db(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("""
            INSERT INTO restaurants (restaurant_name, item_query)
            VALUES (%s, %s)
        """, (self.restaurant_name, self.query))
        db_connection.commit()
        self.id = cursor.lastrowid


class Review:
    def __init__(self, item_query, review_text, rating, sentiment_score):
        self.item_query = item_query
        self.review_text = review_text
        self.rating = rating
        self.sentiment_score = sentiment_score

    def insert_into_db(self, db_connection, restaurant_id):
        cursor = db_connection.cursor()
        cursor.execute("""
            INSERT INTO reviews (restaurant_id, item_query, rating, review_text, sentiment_score)
            VALUES (%s, %s, %s, %s, %s)
        """, (restaurant_id, self.item_query, self.rating, self.review_text, self.sentiment_score))
        db_connection.commit()


class RestaurantReviewDatabase:
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run LOCALLY, this should be localhost
            'port': '32000',  # to run LOCALLY, this should be 32000
            'database': 'reviews'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def insert_restaurant_query(self, query, restaurant_name):
        restaurant = RestaurantQuery(query, restaurant_name)
        restaurant.insert_into_db(self.connection)
        return restaurant

    def insert_reviews(self, reviews, restaurant):
        for review in reviews:
            review.insert_into_db(self.connection, restaurant.id)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
