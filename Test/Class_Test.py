from db.mysql_repository import *
from App.Classes import MenuItem
import pytest
def test_insert_restaurant(restaurant_name, item_query):
    repo = MysqlRepository()

    menu_item = MenuItem(
        restaurant_name=restaurant_name,
        item_query=item_query
    )
    restaurant_id = repo.insert_restaurant(menu_item)
    assert restaurant_id is not None