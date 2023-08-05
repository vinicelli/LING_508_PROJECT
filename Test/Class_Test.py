# Import the required classes
from db.mysql_repository import MysqlRepository
from App.Classes import MenuItem
import pytest

# Define the 'repository' fixture
@pytest.fixture
def repository():
    return MysqlRepository()

def test_insert_restaurant(repository):
    menu_item = MenuItem(
        restaurant_name="Test Restaurant",
        item_query="Test Query"
    )
    restaurant_id = repository.insert_restaurant(menu_item)
    assert restaurant_id is not None

    # Optionally, you can add more assertions or checks here to validate the insertion.
