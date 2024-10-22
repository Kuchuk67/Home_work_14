from decimal import Decimal

class Product:
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


x = Product('товар_1','Описание: товар 1', 124.27, 10)

print(x.price/3)