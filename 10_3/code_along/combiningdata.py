"""
Combining data types
"""
num1 = 3
num2 = num1 + 2

pi = 3.14

word = "hello"

on = True
off = False
foobar = True

# which data type is this?
#input() which take in data from some file stream
y = input("type something here.")

# does this work? why or why not?
#No it wont work because we are adding strings together
print(word + y)

# how about this?
#No we cannot add a numerica value with a string.
print(num1 + word)

# what can we do to make this work?
# to make this work we could maybe turn both into numeric values.
print(num1 + word)

# data-type conversions

# what type do we see here?
# these are numberic values in which we are able produce a value as a result.
print(type(num1 + num1))

# how about here?
#since pi is a defined number and num1 is also defined as well, there should be no problem overall.
print(type(num1 + pi))

# surprises
print(num1 + pi)

# and fixes

# floating point error explained:
#   https://realpython.com/lessons/floating-point-representation-error/

# this isn't a problem for us, unless you need those milliseconds: 
#   http://www.cs.unc.edu/~smp/COMP205/LECTURES/ERROR/lec23/node4.html