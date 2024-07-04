#to handle these exceptions we hava try,except,else and finally

try:
    print("try is executed")
    print(x)
    print(10 / 0)

except ZeroDivisionError:
    print("ZeroDivisionError occurred")
except NameError:
    print("Name error occurred")
else:
    print("no error occurred")
finally:
    print("it will get executed irrespective of try and except")


