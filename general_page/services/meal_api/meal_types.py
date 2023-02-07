from typing import NamedTuple


class MealCategory(NamedTuple):
    """
    Meal category

    :var id_category: str
    :var name_category: str
    :var category_thumb: str
    """
    id_category: str
    name_category: str
    category_thumb: str


class Meal(NamedTuple):
    """
    Meal

    :var id_meal: str
    :var meal_name: str
    :var meal_thumb: str
    """
    id_meal: str
    meal_name: str
    meal_thumb: str


class MealIngredients(NamedTuple):
    """
    Meal ingredients

    :var ingredient_name: str
    :var ingredient_measure: str
    :var ingredient_thumb: str
    """
    ingredient_name: str
    ingredient_measure: str
    ingredient_thumb: str


class MealDetail(NamedTuple):
    """
    Meal detail

    :var meal_name: str
    :var meal_thumb: str
    :var meal_instructions: str
    :var meal_area: str
    :var meal_category: str
    :var meal_tags: str
    :var meal_youtube: str
    :var meal_rate: str
    """
    meal_name: str
    meal_thumb: str
    meal_instructions: str
    meal_area: str
    meal_category: str
    meal_tags: str
    meal_youtube: str
    ingredients: list[MealIngredients]
    meal_rate: str = ''
