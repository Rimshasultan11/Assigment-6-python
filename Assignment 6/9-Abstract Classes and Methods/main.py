# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length , width):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

rect = Rectangle(5, 10)
print(f"Area of rectangle is: {rect.area()}")