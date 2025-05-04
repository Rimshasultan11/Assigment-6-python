# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

class add_greeting:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        instance.greet = lambda: "Hello from Decorator!"
        return instance


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, my name is {self.name}!"


person = Person("Khani")
print(person.say_hello())
print(person.greet())

