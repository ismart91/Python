#passing a member of a class to another class
class Engine:
    def __init__(self):
        self.power=1000
    def start(self):
        print('Engine started')
class Car:
    def __init__(self):
        self.engine=Engine()
    def move(self):
        self.engine.start()
        print('car is moving')
c1=Car()
c1.move()
