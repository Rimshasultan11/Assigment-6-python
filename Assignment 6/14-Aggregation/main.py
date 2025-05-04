# Task
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
      self.name =  name

    def show(self):
       print(f" 👤 Employee Name :{self.name}")

class Department:
   def __init__(self, dept_name, employee):
      self.dept_name = dept_name
      self.employee = employee
    
   def show_details(self):
       print(f" 🏢 Department Name :{self.dept_name}")
       self.employee.show()
        
emp1 = Employee("Rimsha Sultan")

dept1 = Department("IT", emp1)
dept1.show_details()