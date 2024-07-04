class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Child:
    def __init__ (self,school,name,age):
        Parent.__init__(self,name,age)#to avoid we can also use super().__init
        self.school=school

#p1=Parent()
c1=Child("APRS","Siva",19)
#it only wants one arguments since the constructor override the above constructor


