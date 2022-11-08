#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("\nOperations\n")

a = [44, "text", "AC/DC"]
print(type(a))
print(a[1:])
del a[0]
print(a)

print("\nMethods\n")

a = []
b = ["a", "b"]

a.append(1);
print(a)

a.extend(b)
print(a)

print(a.count("a"))

a.remove("a")
print(a)
