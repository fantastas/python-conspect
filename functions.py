#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Positional params

def add(var1, var2):
	res = var1 + var2
	return res

print(add(123,23), "\n")

# Optional params

def opt_add(var1, var2, var3 = 10):
	res = var1 + var2 + var3
	return res

print(opt_add(1,2))
print(opt_add(1,2,3), "\n")

# Key word params

def key_add(var1, var2, var3=10):
	print("var1: %d \t var2: %d \t var3: %d " % (var1,var2,var3) ) 
key_add(1,2,3)