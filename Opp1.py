class Customer:
    Bank_name = 'ABCD'  #class attribute
    def greet(self):

        print(f'Hello welcome to the {self.Bank_name} Bank')
        #self can determine which object is asking for the bank name


#object creation
c1 = Customer()
c1.Bank_name='XYZ'
print(c1.Bank_name)

c2 = Customer()
print(c2.Bank_name)

c2.greet()

#self takes the name of the object

Customer.greet(c1)
