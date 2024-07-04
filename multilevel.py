class A:
    def A(self):
        print('I am the method in class A')
#objects of class A can only access A
class B(A):
    def B(self):
        print('I am the method in class B')
#objects of class B can access both a and b

class C(B):
    def C(self):
        print('I am the method in class C')

#objects of class c can access all a,b,c
obj=C()
obj.A()
obj.B()
obj.C()