# Restaurant Review Sentiment Database

The Restaurant Review Curator is a system that facilitates the management and storage of restaurant reviews along with their associated sentiment scores. The system provides both a user-friendly interface and direct API endpoints for interacting with the database.

## Add a Restaurant

### User Interface (UI)

You can easily add a restaurant to the database using the "Add a Restaurant" interface:

1. Enter the name of the restaurant in the provided input box.
2. Click the "Add Restaurant" button.
3. The system will process your submission and display the response as a JSON string on the page.
4. The restaurant name will be added to the database for later use.

### API Endpoint

You can also add a restaurant directly using a POST request to the following endpoint:

```
POST http://localhost:5000/restaurants
```

The request must include a JSON body with the `name` field, like this:

```json
{
    "name": "Pizza Palace"
}
```

You can use the `curl` command to perform the POST request:

```shell
curl -X POST "http://localhost:5000/restaurants" -H "Content-Type: application/json" -d '{"name":"Pizza Palace"}'
```

## Add a Review

### User Interface (UI)

You can conveniently add a review for a specific menu item using the "Add a Review" interface:

1. Enter the name of the menu item in the provided input box.
2. Click the "Submit" button.
3. The system will process your submission and display the response as a JSON string on the page.
4. The submitted review, along with its sentiment score, will be saved in the database for later retrieval.

### API Endpoint

You can also add a review directly using a POST request to the following endpoint:

```
POST http://localhost:5000/reviews
```

The request must include a JSON body with the `menu_item_name` field, like this:

```json
{
    "menu_item_name": "pizza"
}
```

You can use the `curl` command to perform the POST request:

```shell
curl -X POST "http://localhost:5000/reviews" -H "Content-Type: application/json" -d '{"menu_item_name":"pizza"}'
```

## Fetch All Reviews

To fetch all stored reviews, simply click the "Fetch All Reviews" button. The reviews will be displayed in a list format below the button.

### API Endpoint

Alternatively, you can directly retrieve all reviews using the following API endpoint:

```
GET http://localhost:5000/all-reviews
```

You can use the `curl` command to fetch all reviews:

```shell
curl -X GET "http://localhost:5000/all-reviews"
```

## Search Reviews by Restaurant

If you are looking for reviews specific to a particular restaurant, you can use the "Search Reviews by Restaurant" interface:

1. Enter the name of the restaurant in the input box.
2. Click the "Fetch Reviews" button.
3. The system will display all reviews related to the entered restaurant name.

### API Endpoint

For direct API access, you can retrieve restaurant-specific reviews using the following endpoint:

```
GET http://localhost:5000/reviews-by-restaurant?restaurant_name=RESTAURANT_NAME
```

Replace `RESTAURANT_NAME` with the name of the desired restaurant.

You can use the `curl` command to fetch reviews by restaurant name:

```shell
curl -X GET "http://localhost:5000/reviews-by-restaurant?restaurant_name=Olive%20Garden"
```

## Admin Actions: Clear All Reviews

Administrators or authorized users can clear all reviews from the system by clicking the "Clear All Reviews" button.

### API Endpoint

For direct API access to clear all reviews (note: this may require appropriate privileges):

```
POST http://localhost:5000/clear-reviews
```

You can use the `curl` command to clear all reviews:

```shell
curl -X POST "http://localhost:5000/clear-reviews"
```

---
