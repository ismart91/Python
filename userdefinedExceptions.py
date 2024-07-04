class InvalidAge(Exception):
    pass
n=int(input("enter your age"))
if(n<0):
    raise InvalidAge(f"the age you have entered is {n} which is negative")
print(f"you are {n} years old ")
