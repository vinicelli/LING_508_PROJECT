from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from App.services import *
from App.Classes import *
from db.mysql_repository import MysqlRepository

app = Flask(__name__)
CORS(app)

services = Services()
repo = MysqlRepository()

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
    reviews_list = [review.to_dict() for review in test_reviews]
    return jsonify(reviews_list)


@app.route('/restaurants/<restaurant_name>/reviews', methods=['GET'])
def get_reviews_for_restaurant(restaurant_name):
    reviews = repo.get_reviews_by_restaurant(restaurant_name)
    return jsonify([review.to_dict() for review in reviews])

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
