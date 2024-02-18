import cmath
x = "Hello"
y = True
z = 10.5
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = {"name":"John","age":30}

print("x ,",type(x))
print("y ," ,type(y))
print("z ,",type(z))
print("a ,",type(a))
print("b ,",type(b))
print("c ,",type(c))

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
