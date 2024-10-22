import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def product_1():
    return Product('товар_1','Описание: товар 1', 124.27, 10)


@pytest.fixture
def product_2():
    return Product('товар_2','Описание: товар 2', 148.0023)


@pytest.fixture
def category_1():
    return Category(
        'Категория 1',
        'Категория товаров номер один',
        [ Product('товар_1','Описание: товар 1', 124.27, 10),
        Product('товар_2','Описание: товар 2', 148.0023)]
    )