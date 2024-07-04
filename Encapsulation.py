'''class Car:
    price=500000

c1=Car()
print(c1.price)
c1.price=0
print(c1.price)'''

class Car:
    __price = 500000#private _ means protected
    def display_price(self):
        print(f'the price of the car is {self.__price}')


c1 = Car()
c1.display_price()
