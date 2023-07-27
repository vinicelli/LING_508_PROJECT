import mysql.connector

class MenuItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Review:
    def __init__(self, menu_item, review_text, sentiment_score):
        self.menu_item = menu_item
        self.review_text = review_text
        self.sentiment_score = sentiment_score

class ReviewDatabase:
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db', # to run LOCALLY, this should be localhost
            'port': '3306', # to run LOCALLY, this should be 32000
            'database': 'menu_db'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id INT AUTO_INCREMENT PRIMARY KEY,
                menu_item_name VARCHAR(255),
                review_text TEXT,
                sentiment_score FLOAT
            )
        """)
        self.connection.commit()

    def add_review(self, review):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO reviews (menu_item_name, review_text, sentiment_score)
            VALUES (%s, %s, %s)
        """, (review.menu_item.name, review.review_text, review.sentiment_score))
        self.connection.commit()

    def get_reviews_by_menu_item(self, menu_item_name):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT review_text, sentiment_score
            FROM reviews
            WHERE menu_item_name = %s
        """, (menu_item_name,))
        rows = cursor.fetchall()
        return [Review(MenuItem(menu_item_name), row[0], row[1]) for row in rows]

    def __del__(self):
        self.connection.close()