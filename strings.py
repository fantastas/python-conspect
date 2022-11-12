#!/usr/bin/env python

# -*- coding: utf-8 -*-

# remove whitespace from a string

line = "\n  textas    ..\n\t"

#right
print(line.rstrip())		

#left
print(line.lstrip())

#all whitespaces
print(line.strip()) 

# start & end to the string

print(line.startswith('\n'))
print(line.endswith('\t'))

# f print

m = 4
n = 3

print(f'{m} * {n} = {m*n}')
