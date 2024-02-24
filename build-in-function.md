**Python Built-in Functions**

1. **`print()`**:  
   - Description: Prints the specified message to the screen or console.
   - Example:
     ```python
     print("Hello, world!")
     ```

2. **`len()`**:  
   - Description: Returns the length (the number of items) of an object.
   - Example:
     ```python
     my_list = [1, 2, 3, 4, 5]
     print(len(my_list))  # Output: 5
     ```

3. **`input()`**:  
   - Description: Reads a line of input from the user via the keyboard.
   - Example:
     ```python
     name = input("Enter your name: ")
     ```

4. **`type()`**:  
   - Description: Returns the type of an object.
   - Example:
     ```python
     print(type(10))  # Output: <class 'int'>
     ```

5. **`int()`**, **`float()`**, **`str()`**, **`list()`**, **`tuple()`**, **`dict()`**, **`set()`**:  
   - Description: Convert a value to an integer, float, string, list, tuple, dictionary, or set, respectively.
   - Example:
     ```python
     x = int("10")
     ```

6. **`range()`**:  
   - Description: Generates a sequence of numbers within a specified range.
   - Example:
     ```python
     for i in range(5):
         print(i)  # Output: 0, 1, 2, 3, 4
     ```

7. **`max()`**, **`min()`**:  
   - Description: Returns the maximum or minimum value from a sequence or set of arguments.
   - Example:
     ```python
     numbers = [3, 7, 2, 10]
     print(max(numbers))  # Output: 10
     ```

8. **`sum()`**:  
   - Description: Returns the sum of all the elements in a sequence.
   - Example:
     ```python
     numbers = [1, 2, 3, 4, 5]
     print(sum(numbers))  # Output: 15
     ```

9. **`abs()`**:  
   - Description: Returns the absolute value of a number.
   - Example:
     ```python
     print(abs(-5))  # Output: 5
     ```

10. **`sorted()`**:  
    - Description: Returns a new sorted list from the elements of any iterable.
    - Example:
      ```python
      numbers = [3, 1, 4, 1, 5, 9, 2]
      sorted_numbers = sorted(numbers) # sorted_numbers: [1, 1, 2, 3, 4, 5, 9]
      ```
