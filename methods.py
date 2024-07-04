''''Instance method ,class method and static methods'''
class Student:
    school_name='APRS'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):  #instance method it can access both instance and class level
        print(f'Name {self.name} and age is {self.age}')
    @classmethod  #can only access class level things
    def get_school_name(cls):
        return cls.school_name
    @staticmethod #it neither access class level nor instance variables
    def is_adult(age):
        return age>18
s1=Student('Siva',19)
s1.display()
print(s1.get_school_name())
print(s1.is_adult(18))

