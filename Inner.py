#class with in a class
class Outer:
    def __init__(self):
        self.x=78
        print('outer class executed')
    class Inner:
        def __init__(self):
            print('Inner class executed')
        def display(self):
            print(f'we are accessing the outer class variable x = {self.x}')
out=Outer()
In=out.Inner()
In.display()
