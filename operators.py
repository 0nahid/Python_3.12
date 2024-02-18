x = 10
y = 3
# Addition
print(x + y)  # Output: 13
# Subtraction
print(x - y)  # Output: 7
# Multiplication
print(x * y)  # Output: 30
# Division
print(x / y)  # Output: 3.3333333333333335
# Modulus
print(x % y)  # Output: 1
# Exponentiation
print(x ** y)  # Output: 1000
# Floor division
print(x // y)  # Output: 3
# Comparison operators
x = 10
y = 12
# Greater than
print(x > y)  # Output: False
# Less than
print(x < y)  # Output: True
# Equal to
print(x == y)  # Output: False
# Not equal to
print(x != y)  # Output: True
# Greater than or equal to
print(x >= y)  # Output: False
# Less than or equal to
print(x <= y)  # Output: True
# Logical operators
x = True
y = False
# AND
print(x and y)  # Output: False
# OR
print(x or y)  # Output: True
# NOT
print(not x)  # Output: False
# Identity operators
x = 5
y = 5
# is
print(x is y)  # Output: True
# is not
print(x is not y)  # Output: False
# Membership operators
x = "Hello World"
# in
print("H" in x)  # Output: True
# not in
print("h" not in x)  # Output: True
# Bitwise operators
x = 10
y = 4
# Bitwise AND
# Bitwise AND (&):
# The bitwise AND operator (&) compares the binary representations of two integers and returns a new integer where each bit is set to 1 only if both corresponding bits in the operands are 1.
x = 10   # 1010 in binary
y = 4    # 0100 in binary
result = x & y
print(result)   # Output: 0   (0000 in binary)

# Bitwise OR
# Bitwise OR (|):
# The bitwise OR operator (|) compares the binary representations of two integers and returns a new integer where each bit is set to 1 if at least one of the corresponding bits in the operands is 1.
x = 10   # 1010 in binary
y = 4    # 0100 in binary
result = x | y
print(result)   # Output: 14   (1110 in binary)

# Bitwise XOR
# Bitwise XOR (^):
# The bitwise XOR operator (^) compares the binary representations of two integers and returns a new integer where each bit is set to 1 if exactly one of the corresponding bits in the operands is 1.
x = 10   # 1010 in binary
y = 4    # 0100 in binary
result = x ^ y
print(result)   # Output: 14   (1110 in binary)

# Bitwise NOT
# Bitwise NOT (~):
# The bitwise NOT operator (~) performs a bitwise negation operation on a single integer. It returns the complement of the binary representation of the integer.
x = 10   # 1010 in binary
result = ~x
print(result)   # Output: -11   (The two's complement of 1010 is -11)

# Bitwise left shift
# Bitwise left shift (<<):
# The bitwise left shift operator (<<) shifts the bits of the first operand to the left by the number of positions specified in the second operand. Excess bits shifted off to the left are discarded, and zero bits are shifted in from the right.
x = 10   # 1010 in binary
result = x << 2
print(result)   # Output: 40   (101000 in binary)
