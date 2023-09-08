# int
myint = 7
print(myint)

# float
myfloat = 7.0
print(myfloat)

# int to float
myfloat = float(myint)
print(myfloat)

# string
myStr = "hello python"
print(myStr)

myStr = 'hello python'
print(myStr)

mystring = "Don't worry about apostrophes"
print(mystring)

# Operators
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assignments
a, b = 3, 4
print(a, b)

# This will not work!
one = 1
two = 2
hello = "hello"

#print(one + two + hello)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

""" Exercise
The target of this exercise is to create a string, an integer, and a floating point number. 
The string should be named mystring and should contain the word "hello". 
The floating point number should be named myfloat and should contain the number 10.0, 
and the integer should be named myint and should contain the number 20. """

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)