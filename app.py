from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from App.services import *
from App.Classes import *
from db.mysql_repository import MysqlRepository

app = Flask(__name__)
CORS(app)

services = Services()


@app.route('/')
def doc():
    app.logger.info("doc - Got request")
    with open("App/doc.html", "r") as f:
        return f.read()


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()

    menu_item_name = data.get('menu_item_name')
    if not menu_item_name:
        abort(400, "menu_item_name is required")

    services.add_to_reviews(menu_item_name)
    return jsonify({"message": "Reviews added successfully!"})


@app.route('/reviews', methods=['GET'])
def get_reviews():
    # This is a placeholder, you'll likely want to integrate with your MySQL repo to fetch actual reviews.
    return jsonify(Review.to_dict(test_reviews))


@app.route('/restaurants/<restaurant_name>/reviews', methods=['GET'])
def get_reviews_for_restaurant(restaurant_name):
    # This function can fetch reviews for a particular restaurant.
    # Use the restaurant_name parameter to query your database and return reviews.
    # I'm returning the test_reviews here for demonstration.
    return jsonify([review for review in test_reviews if review.restaurant_name == restaurant_name])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
