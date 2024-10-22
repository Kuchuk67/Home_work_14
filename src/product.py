class Product:
    '''
    класс Product имеет  следующие свойства:
    название,описание ,цена,количество в наличии
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float=0.0, quantity: int=0) ->None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# if __name__ == '__main__':
# x = Product('товар_1','Описание: товар 1', 124.27, 10)

# print(x.price)
