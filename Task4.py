class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, key, value):
        if key == 'price':
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError('Price has to be an integer or float and positive')
        if key == 'quantity':
            if not isinstance(value, int) or value < 0:
                raise ValueError('Quantity has to be an integer and positive')
        super().__setattr__(key, value)

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity = {self.quantity})"


if __name__ == '__main__':
   p1 = Product("Laptop" , 1000 , 8)
   print(p1)