from typing import Optional


class Category:
    '''
        класс Category имеет  следующие свойства:
        название,описание,список товаров категории
        общее количество категорий и количество товаров
        '''
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[list] = None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)


if __name__ == "__main__":
    pass
