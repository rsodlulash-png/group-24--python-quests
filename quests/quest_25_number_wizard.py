#!/usr/bin/python3
secret_number = int(input("Guess the secret number in my mind: "))
while secret_number != 105:
    print("Wrong guess, guess again!")
    if secret_number > 105:
        print("Guess is too high")
    else:
        print("Guess is too low")
    secret_number = int(input("Guess again: "))
print("correct Guess, congratulations")

