class A:
    def A(self):
        print('I am A')
class B(A):
    def B(self):
        print('I am B')
obj=A()
obj.A()
obj=B()
obj.A()
obj.B()

