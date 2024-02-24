def sayHello(x):
    return "Hello " + x

print(sayHello("John"))

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator 

def say_hello():
    print("Hello!")

say_hello()

# Error handling
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(220, 5)