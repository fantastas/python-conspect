#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Changeable and unchangeable data types
# The address of a variable can be read out with the "id"
# command.

print("unchangeable")
a = 10
b = 10
c = 'as'
f = 'as'
print(id(a))
print(id(b))
a = 11
print(id(a))
print("\n")
print(id(c))
print(id(f))


print("changeable")

a = ["x"]
print(id(a))

b = ["x"]
print(id(b))

# variable names must beggin with letter or _
# rest of variable must be a-z, 0-9 or _