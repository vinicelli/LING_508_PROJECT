from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from App.services import *
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

services = Services()

@app.route('/')
def doc():
    app.logger.info("doc - Got request")
    with open("web/reviews.html", "r") as f:
        return f.read()

@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    data = request.get_json()
    name = data.get('name')

    if not name:
        abort(400, "Restaurant name is required")

    services.add_restaurant(name)
    return jsonify({"message": "Restaurant added successfully!"})


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    restaurant_id = data.get('restaurant_id')
    author = data.get('author')
    rating = data.get('rating')
    review_text = data.get('review_text')
    sentiment_score = TextBlob(review_text).sentiment.polarity

    if not restaurant_id or not author or not rating or not review_text:
        abort(400, "All fields are required")

    review = Review(restaurant_id=restaurant_id, author=author, rating=rating, review_text=review_text, sentiment_score=sentiment_score)

    services.add_review(review)

    return jsonify({"message": "Review added successfully!"})


@app.route('/reviews-by-restaurant', methods=['GET'])
def get_reviews_for_restaurant():
    restaurant_name = request.args.get('restaurant_name')
    reviews = services.get_reviews_by_restaurant(restaurant_name)
    return jsonify(reviews)


@app.route('/reviews/<restaurant_name>', methods=['GET'])
def get_reviews(restaurant_name):
    reviews = services.get_reviews_by_restaurant(restaurant_name)
    json_reviews = [
        {
            "id": review.id,
            "restaurant_id": review.restaurant_id,
            "author": review.author,
            "rating": review.rating,
            "review_text": review.review_text,
            "sentiment_score": review.sentiment_score
        }
        for review in reviews
    ]
    return jsonify(json_reviews)


@app.route('/all-reviews', methods=['GET'])
def all_reviews():
    reviews = services.get_all_reviews()
    return jsonify([review.to_dict() for review in reviews])


@app.route('/clear-reviews', methods=['POST'])
def clear_reviews():
    services.clear_all_reviews()
    return jsonify({"message": "All reviews cleared!"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from App.services import *
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

services = Services()


@app.route('/')
def doc():
    app.logger.info("doc - Got request")
    with open("web/reviews.html", "r") as f:
        return f.read()


@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    data = request.get_json()
    name = data.get('name')

    if not name:
        abort(400, "Restaurant name is required")

    services.add_restaurant(name)
    return jsonify({"message": "Restaurant added successfully!"})


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    restaurant_id = data.get('restaurant_id')
    author = data.get('author')
    rating = data.get('rating')
    review_text = data.get('review_text')
    sentiment_score = TextBlob(review_text).sentiment.polarity

    if not restaurant_id or not author or not rating or not review_text:
        abort(400, "All fields are required")

    review = Review(restaurant_id=restaurant_id, author=author, rating=rating, review_text=review_text, sentiment_score=sentiment_score)

    services.add_review(review)

    return jsonify({"message": "Review added successfully!"})


@app.route('/reviews-by-restaurant<restaurant_name>', methods=['GET'])
def get_reviews_for_restaurant():
    restaurant_name = request.args.get('restaurant_name')
    reviews = services.get_reviews_by_restaurant(restaurant_name)
    return jsonify(reviews)


@app.route('/reviews/<restaurant_name>', methods=['GET'])
def get_reviews(restaurant_name):
    reviews = services.get_reviews_by_restaurant(restaurant_name)
    json_reviews = [
        {
            "id": review.id,
            "restaurant_id": review.restaurant_id,
            "author": review.author,
            "rating": review.rating,
            "review_text": review.review_text,
            "sentiment_score": review.sentiment_score
        }
        for review in reviews
    ]
    return jsonify(json_reviews)


@app.route('/all-reviews', methods=['GET'])
def all_reviews():
    reviews = services.get_all_reviews()
    return jsonify([review.to_dict() for review in reviews])


@app.route('/clear-reviews', methods=['POST'])
def clear_reviews():
    services.clear_all_reviews()
    return jsonify({"message": "All reviews cleared!"})


@app.route('/get-restaurant-id<restaurant_name>', methods=['GET'])
def get_restaurant_id_by_name():
    restaurant_name = request.args.get('restaurant_name')

    restaurant_id = services.get_restaurant_id_by_name(restaurant_name)
    return jsonify({'restaurant_id': restaurant_id})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
