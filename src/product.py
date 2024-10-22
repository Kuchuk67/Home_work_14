from decimal import Decimal

class Product:
    name: str
    description: str
    price: Decimal()
    quantity: int


    def __init__(self, name, description, price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

