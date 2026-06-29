#!/usr/bin/python3
#Testing the While Loop and guessing the number.
#Secret Number
secret_No = 66
guess = None
while guess != secret_No:
	guess = int(input("Guess the secret number: "))
if guess != secret_No:
	print("Incorrect quest")
else:
	print("Yayyy, correct guess!")
