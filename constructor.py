class customer:
    Bank_name='HDFC'  #class variable    class level variables
    def __init__(self,name,age,initial_amount):
        print(f'welcome to {self.Bank_name} Bank!!')
        self.name=name    # these are instance variables object level varables
        self.age=age
        self.balance=initial_amount
    def deposit(self,amount):
        self.balance+=amount #amount is the local variable method level variables
        print(f'dear {self.name} The amount {amount} has successfully deposited.updated balance is {self.balance}')

c1=customer('siva',19,10000)
c2=customer('sankar',20,initial_amount=7890)
c2.deposit(7800)