# comments:
# single line by pound symbol
# multiline by 3 quotes
"""
print("hello") 
"""

# Primitive Data Types & Operators
"""
1. Numbers
2. Boolean
"""

# variables are never declared but always assigned. Convention is snake_case


def printMe(x):
    # print(x)
    return x


# Numbers
# Sum
printMe(1+2)

# Multiplication
printMe(10*15)

# Division => always a float
printMe(10/15)

# Integer division => rounded integer value +-
printMe(10//15)

# Modulo
printMe(7 % 3)
printMe(-7 % 3)

# Exponentiation **
printMe("2^3 is: ")
printMe(2**3)

# Boolean
# with capital letter
# True False are actually 1 & 0 thus can be used in numeric computations
printMe(True)
printMe(False)

# using not operator to toggle
printMe(not True)

# and or operators
printMe(True and False)
printMe(True or False)

# numeric True False
# Comparison operators look at the numeric value of the boolean
printMe(8 * False)
printMe(8 * True)
printMe(0 == False)
printMe(1 == True)
printMe(-1 == False)
printMe(-1 == True)

# Casting ints to booleans
printMe(bool(0))
printMe(bool(1))
printMe(bool(10))
printMe(bool(-2))

# Equality & Inequality (== or !=)
printMe(1 == 2)
printMe(1 != 2)

# Other comparison operators
printMe(1 > 2)
printMe(1 < 2)
printMe(1 >= 2)
printMe(1 <= 2)

# check if a value is in some range
# say between 1 and 3
printMe(1 < 2 and 2 < 3)

# chaining makes it more readable
printMe(1 < 2 < 3)

# the 'is' operator: checks if two values point to same reference
# == checks if the value is same
a = [1, 2, 3]
b = a
printMe("b is a | b == a")
printMe(b is a)
printMe(b == a)

printMe("reassign b")
b = [1, 2, 3]
printMe("a == b | a is b")
printMe(a == b)
printMe(a is b)


# String: can be created by either " or '
# Concatenation
a = "alpha"
b = "beta"
printMe(a + " woohooo " + b)

# string literals (but not variables) can be concatenated without the + sign
printMe("alpha " "beta")

# strings can be treated as a list of chars, index must be a valid index
printMe("alpha"[1])
printMe(a[3])

# length of a string
printMe(len(a))


# Format strings or f-strings
name = "AYK"
printMe(f"My name is {name} and is {len(name)} chars long")

# None is an object
# use is for checking validity
printMe("abc" == None)
printMe("abc" is None)
printMe(None is None)
printMe(None == None)

# bool can check for truthy or falsy values
# can also check for empty dicts, tuples, lists  etc
printMe(bool(""))
printMe(bool({}))
printMe(bool([]))
printMe(bool(()))
printMe(bool(0))
printMe(bool("0"))

# Getting input from terminal
# input_string = input("Please type your name")
# printMe(f"Name entered is: {input_string}")

# ternary operator
printMe("success" if 1 == True else "false")


# Lists
li = []
li.append(1)
li.append(2)
li.append([1, 2])
printMe(li)

printMe(li.pop())
printMe(li)

# can be accessed like normal arrays using an inbound index

# List slicing [start : end] => end index in not included
li_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("item at index 1")
print(li_2[1])
print("item at index -1")
#  negative index points to last elemnt
print(li_2[-5])

print("list starting from index 1 till end")
print(li_2[1:])

print("list starting from index 1 till 3")
print(li_2[1:3])

print("list from beginning till 3")
print(li_2[:3])

print("list selecting every 3rd element")
print(li_2[::3])

print("list in reverse order")
print(li_2[::-1])
