from typing import Generator

import requests
from .meal_types import MealCategory, Meal, MealDetail
from ..сhatsonic_api.сhatsonic_service import get_answer

API_URL = 'https://www.themealdb.com/api/json/v1/1/'


def get_meal_categories() -> Generator[MealCategory, MealCategory, None]:
    """
    Get meal categories from API themealdb

    :return: Generator[MealCategory, MealCategory, None]
    """

    for category in _create_request('categories.php', '')['categories']:
        yield MealCategory(
            id_category=category['idCategory'],
            name_category=category['strCategory'],
            category_thumb=category['strCategoryThumb']
        )


def get_all_meal() -> Generator[Meal, Meal, None]:
    """
    Get all dishes from API themealdb

    :return: Generator[Meal, Meal, None]
    """
    _categories = _get_list_categories()

    for category in _categories:
        for meal in get_all_meals_by_category(category):
            yield meal


def get_meal_by_id(meal_id: str) -> MealDetail:
    """
    Get meal by id from API themealdb

    :param meal_id: str
    :return: MealDetail
    """
    meal = _create_request('lookup.php', f'?i={meal_id}')['meals'][0]

    return MealDetail(
        meal_name=meal['strMeal'],
        meal_thumb=meal['strMealThumb'],
        meal_instructions=meal['strInstructions'].replace('\r\n', '<br>'),
        meal_area=meal['strArea'],
        meal_category=meal['strCategory'],
        meal_tags=meal['strTags'],
        meal_youtube=meal['strYoutube'],
        meal_rate=get_answer(meal['strMeal']).rate,
    )


def get_all_meals_by_category(category: str) -> Generator[Meal, Meal, None]:
    """
    Get all meals by category

    :param category: str
    :return: Generator[Meal, Meal, None]
    """
    for meal in _create_request('filter.php', f'?c={category}')['meals']:
        yield Meal(
            id_meal=meal['idMeal'],
            meal_name=meal['strMeal'],
            meal_thumb=meal['strMealThumb'],
        )


def _create_request(type_: str, query: str) -> dict | None:
    """
    Create request to API themealdb

    :param type_: str (categories.php, search.php, lookup.php, randomselection.php, etc.)
    :param query: str (query for search)
    :return: dict | None
    """
    response = requests.get(API_URL + type_ + query)

    return response.json() if response.status_code == 200 else None


def _get_list_categories() -> list[str]:
    """
    Get list categories from API themealdb

    :return: list[str]
    """
    return [category['strCategory'] for category in _create_request('list.php', '?c=list')['meals']]
