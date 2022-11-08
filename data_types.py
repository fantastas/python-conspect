#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Data type groups are:
# Numeric types
# Sequential types
# Mappings (Dictionary)

print("\033[1m" + "None type" + "\033[0m")
a = None
print(a); print(type(a))
print(a is None)


"""
int 	Integer, whole numbers, up to 2^64 on 64-bit machines
long 	Long integer, whole numbers, infinitely long, limited by the memory
float 	Floating point numbers
complex Complex numbers
bool 	Boolean values (True or False)

"""
print("\033[1m" + "Numeric types" + "\033[0m")

a = 10
print(type(a))
a = 3.4
print(type(a))
a = 2 + 3j
print(type(a))
a = True
print(type(a))

print("\033[1m" "Sequantial types" +"\033[0m")

# Strings Lists and Tuple
a = """This is a multiline
string."""
print(a)

a = "taip"
b = "dabar"

# bold text
print("\033[1m" + "Operations" + "\033[0m")
print(a + b)
print(a * 3)
print(a[1])
print(b[2:4])
print(len(a))
print("ab" in b)

print("\033[1m" + "Methods" + "\033[0m")

print(b.find("a"))
print(b.count("a"))
print(a.replace("ip", "vo"))
print(a.upper())
print(a.lower())

a = "Test string";
print(a.split());

print("\033[1m" + "Formatting" + "\033[0m")


a = "He is %d years old." % (40)
print(a);
a = "The value is %.2f ." % (1.234567)
print(a);







