# Restaurant Review Curator

In its current iteration the Review Curator searches a compiled list of Review objects and adds them to a database along with their stored sentiment score.

The API can be called using curl commands or using the provided html UI in reviews.html

## Add a Review
You can add a review for a specific menu item using the "Add a Review" interface.
Enter the name of the menu item in the box provided and click "Submit".
After submission, the page will display the response of the submitted review as a JSON string. The review is saved in the database and can be fetched later.

The API can be called directly without the UI, using a POST request.
The endpoint is `http://localhost:5000/reviews`.
The POST request must contain a JSON body with the `"menu_item_name"` key, for example:
```json
{"menu_item_name": "pizza"}
```
A complete `curl` command looks like this:
```shell
curl -X POST "http://localhost:5000/reviews" -H "Content-Type: application/json" -d '{"menu_item_name":"pizza"}'
```

## Fetch All Reviews
To fetch all stored reviews, simply click the "Fetch All Reviews" button. The reviews will be displayed in a list format beneath the button. 

The API endpoint for fetching all reviews is:
```
http://localhost:5000/all-reviews
```

To fetch all reviews using `curl`:
```shell
curl -X GET "http://localhost:5000/all-reviews"
```

## Search Reviews by Restaurant
To find reviews specific to a restaurant, use the "Search Reviews by Restaurant" interface. Enter the restaurant's name and click the respective button. All reviews related to the entered restaurant name will be displayed.

The direct API endpoint for this functionality is:
```
http://localhost:5000/reviews-by-restaurant?restaurant_name=RESTAURANT_NAME
```
Replace `RESTAURANT_NAME` with the desired restaurant's name.

Example using `curl`:
```shell
curl -X GET "http://localhost:5000/reviews-by-restaurant?restaurant_name=Olive Garden"
```

## Admin Actions: Clear All Reviews
Administrators or users with the required privileges (at this stage, anyone) can clear all reviews from the system by clicking the "Clear All Reviews" button.

The direct API call to achieve this, which might be restricted to specific users or require authentication, is:
```
http://localhost:5000/clear-reviews
```
Example using `curl`:
```shell
curl -X POST "http://localhost:5000/clear-reviews"
```

---
