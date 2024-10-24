from src.category import Category


def test_category(category_1):
    assert category_1.name == "Категория 1"
    assert category_1.description == "Категория товаров номер один"
    assert Category.category_count == 1
    assert Category.product_count == 2
