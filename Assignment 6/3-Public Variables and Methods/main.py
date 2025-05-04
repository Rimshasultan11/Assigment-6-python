# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting...")

my_car = Car("BMW")
print(my_car.brand)  # Accessing the public variable
my_car.start()  # Calling the public method        