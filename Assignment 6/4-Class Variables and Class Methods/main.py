# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = 'HBL Bank'

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
    def display(self):
        print(f'Account holder: {self.account_holder} , bank:{self.bank_name}')


account1 = Bank("Rimsha")
account2 = Bank("Faizan")

account1.display()
account2.display()

Bank.change_bank_name("Faizan bank")

account1.display()
account2.display()
