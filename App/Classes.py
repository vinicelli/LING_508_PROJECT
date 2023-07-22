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
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews_by_menu_item(self, menu_item_name):
        return [review for review in self.reviews if review.menu_item.name == menu_item_name]

    def __str__(self):
        return "\n".join(str(review) for review in self.reviews)
