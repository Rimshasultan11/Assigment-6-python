# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        print(f"Number of objects created are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()

Counter.get_count()
