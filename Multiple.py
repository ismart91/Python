class A:
    def A(self):
        print('I am from A')
class B:
    def B(self):
        print('I am from B')
class C(A,B):
    def C(self):
        print('I am from C')
obj=C()
obj.A()
obj.B()
obj.C()
