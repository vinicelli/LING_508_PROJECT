class TestDatabaseCreation(unittest.TestCase):
    def test_database_connection(self):
        # Test if the database connection is successful
        try:
            db = RestaurantReviewDatabase()
            self.assertTrue(isinstance(db.connection, mysql.connector.MySQLConnection))
        except Exception as e:
            self.fail(f"Database connection failed with error: {e}")

    def test_restaurants_table_exist(self):
        # Test if the 'restaurants' table exists in the database
        try:
            db = RestaurantReviewDatabase()
            cursor = db.connection.cursor()
            cursor.execute("SHOW TABLES LIKE 'restaurants'")
            table_exists = cursor.fetchone()
            self.assertIsNotNone(table_exists, "Table 'restaurants' does not exist.")
        except Exception as e:
            self.fail(f"Error occurred while checking the 'restaurants' table: {e}")

    def test_reviews_table_exist(self):
        # Test if the 'reviews' table exists in the database
        try:
            db = RestaurantReviewDatabase()
            cursor = db.connection.cursor()
            cursor.execute("SHOW TABLES LIKE 'reviews'")
            table_exists = cursor.fetchone()
            self.assertIsNotNone(table_exists, "Table 'reviews' does not exist.")
        except Exception as e:
            self.fail(f"Error occurred while checking the 'reviews' table: {e}")


if __name__ == "__main__":
    unittest.main()