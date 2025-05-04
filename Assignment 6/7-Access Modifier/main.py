# task
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
     
    def get_ssn(self):
        return self.__ssn
    
    def get_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Salary must be positive number")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department
    
    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self._salary}")
        print(f"Accessing SSN: {self.get_ssn()}")
    
m = Manager("John Doe", 50000, "123-45-6789", "HR")
m.show_manager_info()
m.get_salary(60000)
print(f"Updated Salary: {m._salary}")

print("Private SSN via managed:", m._Employee__ssn) # This will raise an error because __ssn is private and cannot be accessed directly from outside the class.