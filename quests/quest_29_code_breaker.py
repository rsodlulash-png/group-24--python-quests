secret_code = 42
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts} - Guess the secret code: "))
    #1. Checks if the secret code is correct 
    if guess == secret_code:
        print("Success! You broke the code!")
    #2. If the secret code is correct the program ends
        break
    else:
    #3. if it is not correct you try again 2 times
        if attempt < max_attempts:
            print("Incorrect guess, try again!")
    #4. Lastly if there is no correct attempt
        else:
            print("Incorrect. Game over! You ran out of attempts.")
