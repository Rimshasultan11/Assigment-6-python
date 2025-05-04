# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting Price...")
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Setting New Price..")
            self._price = new_price
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Deleting Price...")
        del self._price

p = Product(100)
print(p.price)
p.price = 150
print(p.price)
del p.price

