import pytest
from src.product import Product

def test_product(product_1):
    assert product_1.name == 'товар_1'
    assert product_1.description == 'Описание: товар 1'
    assert product_1.price == 124.27
    assert product_1.quantity == 10


def test_product(product_2):
    assert product_2.name == 'товар_2'
    assert product_2.description == 'Описание: товар 2'
    assert product_2.price == 148.0023
    assert product_2.quantity == 0