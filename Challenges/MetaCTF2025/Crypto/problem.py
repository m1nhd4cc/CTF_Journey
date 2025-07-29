#!/usr/bin/env python3
import numpy
import random
import base64

OUTPUT_LENGTH = 32

sysrand = random.SystemRandom()
a = []
b = []

def keygen():
	for i in range(0, OUTPUT_LENGTH):
		row = []
		for j in range(0, OUTPUT_LENGTH):
			row.append(sysrand.randint(0, 255))
		a.append(row)
	for i in range(0, OUTPUT_LENGTH):
		b.append(sysrand.randint(0, 255))

def randgen(seed):
	matblock = [c for c in seed]
	npa = numpy.array(a)
	npb = numpy.array(b)
	npmatblock = numpy.array(matblock)
	rand_matrix = [val % 256 for val in numpy.add(numpy.matmul(npa, npmatblock), npb).tolist()]
	return bytes(rand_matrix)

keygen() #This is the only time keygen() is called.
print("Welcome to our little challenge, where you'll try to predict values that are outputted by my random number generator!")
print("I'll give you access to the random generator so you can try it out first. When you're done, you can start the challenge.")
print("The challenge is to guess correctly 50 random outputs in a row. Since this generator is designed to be secure even when the seed is compromised, I'll give you the seed used during each random function call.")
print("Note that inputs and outputs to this game are base64 encoded. Good luck!")
while True:
	print("1) Use the random number generator")
	print("2) Start the challenge")
	print("3) Exit")
	choice = input("> ")
	if "1" in choice:
		print("Enter the base64-encoded seed you want to use:")
		seed = base64.b64decode(input("> "))
		if len(seed) != OUTPUT_LENGTH:
			print("Incorrect seed length.")
			continue
		output = base64.b64encode(randgen(seed))
		print("The base64-encoded random bytes are: " + output.decode("UTF-8"))
	elif "2" in choice:
		print("Good luck!")
		for count in range(0, 50):
			seed = []
			for i in range(0, OUTPUT_LENGTH):
				seed.append(sysrand.randint(0, 255))
			print("base64-encoded seed: " + base64.b64encode(bytes(seed)).decode("UTF-8"))
			print("What is the random output going to be? (base64-encoded)")
			guess = base64.b64decode(input("> "))
			if len(guess) != OUTPUT_LENGTH or randgen(bytes(seed)) != guess:
				print("Incorrect guess! Better luck next time!")
				exit()
			else:
				print("Nicely done!")
		print("Wow guess my random generator isn't as secure as I had thought! Anyways here is the flag: " + "[redacted]")
		exit()
	elif "3" in choice:
		print("Better luck next time!")
		exit()
	else:
		print("Unknown input")
