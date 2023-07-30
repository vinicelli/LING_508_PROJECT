CREATE DATABASE reviews;

CREATE TABLE restaurants (

    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_name VARCHAR(255),
    item_query VARCHAR(255)


)

CREATE TABLE reviews  (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT,
    item_query_id INT,
    author VARCHAR(255),
    rating FLOAT,
    review_text TEXT,
    sentiment_score FLOAT,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
    FOREIGN KEY (item_query_id) REFERENCES restaurants(id)



)

