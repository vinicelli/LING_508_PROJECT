class MenuQuery:
    def __init__(self, restaurant_name, item_query, id=None):
        self.id = id
        self.restaurant_name = restaurant_name
        self.item_query = item_query

class Review:
    def __init__(self, restaurant_id, author, rating, review_text, sentiment_score, id=None):
        self.id = id
        self.restaurant_id = restaurant_id
        self.author = author
        self.rating = rating
        self.review_text = review_text
        self.sentiment_score = sentiment_score

    def search_review_text(self, keyword):

        return keyword.lower() in self.review_text.lower()

