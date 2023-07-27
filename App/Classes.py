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

