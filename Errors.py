class InvalidInput(Exception):
    pass
distance=int(input("Enter the distance in meters : "))
time=int(input("Enter the time in seconds : "))
if(distance<0 or time<0):
    raise InvalidInput("you should not give negative inputs")
try:
    speed=distance/time
    print(f"the speed is {speed}")
except ZeroDivisionError:
    print("You are trying to divide a number with zero")
except NameError:
    print("you are trying to access an undefined object")
else:
    print("there is no error")
finally:

    print("there are some statements below this 4th line")