#!/usr/bin/env python

var = 6


#if loop
if(var < 5):
	print("less than 5")
elif(var < 7):
	print("less than 7 but greater-equal 4")
else:
	print("greater-equal 7")


# while-else loop
while var > 0:
	print(var)
	var = var - 1
else:
	print("while condition is False")

#for loop

myList = (1, 4, 7, 8, 6)
for loopvar in myList:
	print(loopvar)
else:
	print("done")

# range(start,stop,step)

for x in range(10, 20, 3):
	print(x)

# enumerate()

myLetters = ["a", "x", "m"]

for count, x in enumerate(myLetters):
	print(count, x)


# break out of the loop

c = 5

while c > 0:
	print(c)

	if(c < 3):
		break
	c = c - 1
else:
	print("While condition is False")

# continue terminates only current loop cycle

myString = "abcdz"

for letter in myString:
	if letter == "a":
		continue
	if letter == "b":
		continue
	if letter == "z":
		break
	print(letter)










