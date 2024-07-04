''''Define the BankAccount class:
Attributes:
account_number
account_holder
balance
Methods:
__init__(self, account_number, account_holder, balance=0.0): Constructor to initialize account details.
deposit(self, amount): Method to deposit money into the account.
withdraw(self, amount): Method to withdraw money from the account.
get_balance(self): Method to check the balance.
display_account_details(self): Method to display account details.'''


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Hello{self.account_holder} R.S{amount} has been deposited successfully")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print(f"Hello{self.account_holder} amount insufficient to withdraw")

    def balance(self):
        print(f"Balance : {self.balance}")

    def display_account_detailes(self):
        print("___________________")
        print("name : ", self.account_holder)
        print("account number : ", self.account_number)
        print("balance : ", self.balance)

c1 = BankAccount("213312122", "siva", 890)
c2=BankAccount("213345666","sankar")
c1.withdraw(300)
c1.display_account_detailes()
#c2.withdraw(45)
c2.display_account_detailes()