try:
    a=int(input("Enter a number: "))
    result=100/a
    print("Result:", result)
except ValueError:
    print("Please enter digits only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("no error happened")
finally:
    print("program finished")