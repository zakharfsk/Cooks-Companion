from typing import NamedTuple


class MealCategory(NamedTuple):
    id_category: str
    name_category: str
    category_thumb: str


class Meal(NamedTuple):
    id_meal: str
    meal_name: str
    meal_thumb: str


class MealDetail(NamedTuple):
    meal_name: str
    meal_thumb: str
    meal_instructions: str
    meal_area: str
    meal_category: str
    meal_tags: str
    meal_youtube: str
    meal_rate: str = ''
