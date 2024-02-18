# Python Loops README

Welcome to the Python Loops README! This guide provides an overview of loops in Python programming.

## Table of Contents

1. [Introduction to Loops](#introduction-to-loops)
2. [While Loop](#while-loop)
3. [For Loop](#for-loop)
4. [Loop Control Statements](#loop-control-statements)
5. [Nested Loops](#nested-loops)

## Introduction to Loops

Loops in programming are used to execute a block of code repeatedly as long as a specified condition is true. Python supports two main types of loops: the `while` loop and the `for` loop.

## While Loop

The `while` loop repeats a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.

**Syntax:**
```python
while condition:
    # Code block to be executed
```

**Example:**
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
Output:
```
0
1
2
3
4
```

## For Loop

The `for` loop iterates over a sequence (such as a list, tuple, string, or range) and executes a block of code for each element in the sequence.

**Syntax:**
```python
for element in sequence:
    # Code block to be executed
```

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

## Loop Control Statements

Python provides loop control statements to change the execution flow of loops.
- `break`: Terminates the loop prematurely.
- `continue`: Skips the current iteration and proceeds to the next iteration.
- `pass`: Acts as a placeholder and does nothing. It is used when a statement is syntactically required but you want to do nothing.

**Example (break):**
```python
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
```
Output:
```
0
1
2
3
```

## Nested Loops

You can nest one or more loops inside another loop to create nested loops.

**Example:**
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
Output:
```
0 0
0 1
1 0
1 1
2 0
2 1
```