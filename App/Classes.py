from textblob import TextBlob


class Restaurant:
    def __init__(self, restaurant_name, id=None):
        self.id = id
        self.restaurant_name = restaurant_name


class Review:
    def __init__(self, restaurant_id, author, rating, review_text, sentiment_score, id=None):
        self.id = id
        self.restaurant_id = restaurant_id
        self.author = author
        self.rating = rating
        self.review_text = review_text
        self.sentiment_score = sentiment_score

    def to_dict(self):
        return {
            "id": self.id,
            "restaurant_id": self.restaurant_id,
            "author": self.author,
            "rating": self.rating,
            "review_text": self.review_text,
            "sentiment_score": self.sentiment_score
        }

    def search_review_text(self, keyword):

        return keyword.lower() in self.review_text.lower()

    @staticmethod
    def list_to_reviews(review_list, restaurant_id):
        reviews = []
        for data in review_list:
            author = data[0]
            rating = data[1]
            review_text = data[2]
            sentiment_score = TextBlob(review_text).sentiment.polarity
            review = Review(restaurant_id, author, rating, review_text, sentiment_score)
            reviews.append(review)
        return reviews
