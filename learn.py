#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Practising python syntax")

#; to keep in same line
a = 3; print(a)

myString = "This is a \
long string. \
this string is wrtten \
in 4 lines."

print(myString)


"""Begin of multiline comment.
And another line of comment."""

#string concatination 
print(str(a) + "\n" + myString)

"""print() usually ends with new line
to avoid it use an 'end' argument"""

print("like", end = " ")
print("this")

# raw_input() for user input
#char() Conversion from number to letter
#ord() Conversion from letter to number

inputVar = input("Please enter a number:")
print("type before conversiont is: ", type(inputVar))

inputNumber = int(inputVar)
print("type after conversion is:", type(inputNumber))

b = 'a'
print(ord(b))

