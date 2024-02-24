# Functions in Python

Functions are a fundamental concept in Python programming, allowing you to organize code into reusable blocks for better modularity and maintainability. This README provides an overview of functions in Python, covering basic syntax, advanced usage, and best practices.

## Table of Contents

- [Basics of Functions](#basics-of-functions)
- [Function Arguments](#function-arguments)
- [Return Statement](#return-statement)
- [Scope and Lifetime of Variables](#scope-and-lifetime-of-variables)
- [Lambda Functions (Anonymous Functions)](#lambda-functions-anonymous-functions)
- [Recursion](#recursion)
- [Built-in Functions](#built-in-functions)
- [Function Decorators](#function-decorators)
- [Documentation and Docstrings](#documentation-and-docstrings)
- [Best Practices](#best-practices)
- [Error Handling](#error-handling)
- [Function Annotations (Optional)](#function-annotations-optional)

## Basics of Functions

Functions in Python are defined using the `def` keyword followed by the function name and parameters, if any. They can be called using the function name followed by parentheses. Example:

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Output: Hello, Alice!
```

## Function Arguments

Python functions can accept positional arguments, keyword arguments, default arguments, and variable-length arguments. This provides flexibility in how functions are called and used. Example:

```python
def add(x, y=0):
    return x + y

print(add(2, 3))  # Output: 5
print(add(2))     # Output: 2 (default argument used)
```

## Return Statement

The `return` statement is used to return values from a function. Functions can return multiple values as a tuple. Example:

```python
def square_and_cube(x):
    return x ** 2, x ** 3

result = square_and_cube(3)
print(result)  # Output: (9, 27)
```

## Scope and Lifetime of Variables

Variables in Python have different scopes: global and local. Understanding variable scope is crucial for writing functions that behave as expected. Example:

```python
x = 10  # Global variable

def func():
    y = 20  # Local variable
    print(x)  # Access global variable
    print(y)

func()
```

## Lambda Functions (Anonymous Functions)

Lambda functions are small anonymous functions that can be defined using the `lambda` keyword. They are often used for short functions. Example:

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

## Recursion

Recursion is a programming technique where a function calls itself. It's useful for solving problems that can be broken down into smaller, similar subproblems. Example:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

## Built-in Functions

Python provides many built-in functions for common tasks such as string manipulation, mathematical operations, and data manipulation. Example:

```python
print(len("hello"))  # Output: 5
print(max(3, 7, 2))  # Output: 7
```

## Function Decorators

Function decorators are a powerful feature in Python for modifying the behavior of functions. They are often used for logging, caching, and authentication. Example:

```python
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
```

## Documentation and Docstrings

Documenting your functions using docstrings helps other developers understand how to use your code. It also facilitates automated documentation generation. Example:

```python
def add(x, y):
    """Add two numbers."""
    return x + y
```

## Best Practices

Follow best practices for naming functions, choosing function arguments, and writing modular, reusable code. Write testable functions and unit tests for your code.

## Error Handling

Handle errors and exceptions within functions using `try` and `except` blocks. Raise exceptions when necessary.

## Function Annotations (Optional)

Annotate function arguments and return types for better readability and type hinting. Example:

```python
def greet(name: str) -> str:
    return "Hello, " + name + "!"
```
