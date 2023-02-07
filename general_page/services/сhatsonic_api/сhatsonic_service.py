import os
import re

import requests

from .сhatsonic_types import DishesRate

API_URL = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"


def get_answer(name_dishes: str) -> DishesRate:
    """
    Get answer from AI how difficult it is to cook dishes

    :param name_dishes: str
    :return: str | None
    """
    payload = {
        "enable_google_results": "true",
        "enable_memory": False,
        "input_text": f"How difficult it is to cook '{name_dishes}' on a scale of 1 to 10."
                      "Give me answer in format - number/number."
                      "For example 5/10"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": os.getenv('WRITESONIC_API_KEY')
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    return DishesRate(rate=_parse_ai_answer(response.json()['message']) if response.status_code == 200 else None)


def _parse_ai_answer(answer: str) -> str | None:
    """
    Parse answer from AI

    :param answer: str - answer from AI
    :return: list[str] | None - [number/number, number/number, ...]
    """
    matches = re.compile(r'\d+/\d+').findall(answer)

    return matches[0] if matches else None
