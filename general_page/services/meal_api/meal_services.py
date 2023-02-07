import requests
from .meal_types import MealCategory

API_URL = 'https://www.themealdb.com/api/json/v1/1/'


def _create_request(type_: str, query: str) -> dict | None:
    """
    Create request to API themealdb

    :param type_: str (categories.php, search.php, lookup.php, randomselection.php, etc.)
    :param query: str (query for search)
    :return: dict | None
    """
    response = requests.get(API_URL + type_ + query)

    return response.json() if response.status_code == 200 else None


def get_meal_categories() -> list[MealCategory] | None:
    """
    Get meal categories from API themealdb

    :return: list[dict] | None
    """

    for category in _create_request('categories.php', '')['categories']:
        yield MealCategory(
            id_category=category['idCategory'],
            name_category=category['strCategory'],
            category_thumb=category['strCategoryThumb']
        )


def get_meal_by_id(meal_id: str) -> dict | None:
    pass