#!/usr/bin/env python

a = {"Joe": "red", "Henry": "green", "Adam": "orange"}
print(type(a))

print("\nOperations\n")

print(a["Joe"])
print("Adam" in a)
del(a["Henry"])
print(a)

print("\nMethods\n")

print(a.keys())
print(a.values())
