class Category:
    name: str
    description: str
    products: list

    quantity_category = 0
    quantity_products = 0

    def __init__(self, name, description, products = None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.quantity_category += 1
        Category.quantity_products += len(self.products)
