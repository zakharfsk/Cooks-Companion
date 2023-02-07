from typing import NamedTuple


class DishesRate(NamedTuple):
    """
    Dishes rate

    :var rate: str | None
    """
    rate: str | None


class RandomRecipe(NamedTuple):
    """
    Random recipe

    :var recipe: str
    :var image: str
    """
    recipe: str
    image: str