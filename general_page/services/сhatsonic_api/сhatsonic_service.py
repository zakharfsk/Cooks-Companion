import os
import re

import requests

from .сhatsonic_types import DishesRate, RandomRecipe

API_URL = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"


def get_answer(name_dishes: str) -> DishesRate:
    """
    Get answer from AI how difficult it is to cook dishes

    :param name_dishes: str
    :return: str | None
    """

    response, status_code = _create_request(
        f"How difficult it is to cook '{name_dishes}' on a scale of 1 to 10."
        f"Give me answer in format - number/number."
        f"For example 5/10"
    )

    return DishesRate(rate=_parse_ai_answer(response) if status_code == 200 else None)


def get_random_recipe() -> RandomRecipe:
    """
    Get random recipe from AI

    :return: str | None
    """
    response, status_code = _create_request(
        f"Give me random meal recipe and correct photo. Search photo on pexels.com"
    )

    return RandomRecipe(recipe=response.replace('\n', '<br>'), image=_get_image_from_string(response)) if status_code == 200 else None


def _create_request(input_text: str) -> tuple[str, int]:
    """
    Create request to AI

    :param input_text: str
    :return: tuple[str, int]
    """
    payload = {
        "enable_google_results": "true",
        "enable_memory": False,
        "input_text": input_text
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": os.getenv('WRITESONIC_API_KEY')
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    return response.json()['message'], response.status_code


def _parse_ai_answer(answer: str) -> str | None:
    """
    Parse answer from AI

    :param answer: str - answer from AI
    :return: list[str] | None - [number/number, number/number, ...]
    """
    matches = re.compile(r'\d+/\d+').findall(answer)

    return matches[0] if matches else None


def _get_image_from_string(answer: str) -> str | None:
    """
    Parse answer from AI and get image

    :param answer: str - answer from AI
    :return: list[str] | None - [number/number, number/number, ...]
    """
    matches = re.compile(r'(https?://[^\s]+\?[^\s]+)').findall(answer)[0][:-1]

    return matches if matches else None
