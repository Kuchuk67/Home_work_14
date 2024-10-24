import json
import os
from typing import Any

from config import PATH_HOME
from src.category import Category
from src.product import Product


def read_json(file: str) -> Any:
    path_to_file = os.path.join(PATH_HOME, "data", file)
    with open(path_to_file, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def upload_products_from_json(categories: dict) -> list:
    list_categories = []
    for category in categories:
        prod_list = []
        for product in category.get("products", []):
            prod_list.append(Product(**product))
        category["products"] = prod_list
        list_categories.append(Category(**category))

    return list_categories
