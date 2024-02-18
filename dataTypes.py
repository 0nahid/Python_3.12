import cmath
x = "Hello"  # Example: a string
y = True     # Example: a boolean
z = 10.5     # Example: a float
a = [1, 2, 3, 4, 5]  # Example: a list
b = (1, 2, 3, 4, 5)  # Example: a tuple
c = {"name": "John", "age": 30}  # Example: a dictionary

print("x ,", type(x))  # Output: x , <class 'str'>
print("y ,", type(y))  # Output: y , <class 'bool'>
print("z ,", type(z))  # Output: z , <class 'float'>
print("a ,", type(a))  # Output: a , <class 'list'>
print("b ,", type(b))  # Output: b , <class 'tuple'>
print("c ,", type(c))  # Output: c , <class 'dict'>

# Integers
my_integer = 42
print("my_integer ,", type(my_integer))  # Output: <class 'int'>

# Complex numbers
my_complex = 3 + 4j
print("my_complex ,", type(my_complex))  # Output: <class 'complex'>

my_complex = 3 + 4j
print("Real part:", my_complex.real)  # Output: 3.0
print("Imaginary part:", my_complex.imag)  # Output: 4.0
print("Magnitude:", abs(my_complex))  # Output: 5.0 (magnitude or absolute value)
print("Phase angle:", cmath.phase(my_complex))  # Output: 0.9272952180016122 (phase angle)

# Bytes
my_bytes = b"hello"
print("my_bytes ,", type(my_bytes))  # Output: <class 'bytes'>

# Bytearray
my_bytearray = bytearray(b"world")
print("my_bytearray ,", type(my_bytearray))  # Output: <class 'bytearray'>

# Set
my_set = {1, 2, 3}
print("my_set ,", type(my_set))  # Output: <class 'set'>

# Frozenset
my_frozenset = frozenset({4, 5, 6})
print("my_frozenset ,", type(my_frozenset))  # Output: <class 'frozenset'>

# NoneType (None)
my_none = None
print("my_none ,", type(my_none))  # Output: <class 'NoneType'>
