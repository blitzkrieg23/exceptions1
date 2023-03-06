def divide(a,b):
    return a/b

try:
   divide(5/0)


#except Exception as e:
except ZeroDivisionError as e:
    print(e,"We cannot divide by zero!")
