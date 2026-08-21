"""
EXERCISE 03 - Number guessing game
Topic: while + break + input()

TASK
----
The computer picks a secret number from 1 to 20.
Keep asking the user to guess until they get it right.
After each wrong guess print "Too high" or "Too low".
When they get it right, print how many guesses it took, then break.

Give the user a maximum of 5 attempts. If they run out, reveal the answer.

HINTS
-----
* input() always returns a STRING - convert it with int()
* a while loop needs something that changes, or it runs forever
* Ctrl + C in the terminal stops a runaway program

SAMPLE RUN
----------
Guess a number between 1 and 20: 10
Too low
Guess a number between 1 and 20: 15
Too high
Guess a number between 1 and 20: 13
Correct! You took 3 guesses.
"""


# TODO: write the while loop here.
#       1. increase attempts
#       2. read a guess with input() and convert it to int
#       3. compare it with secret and print Too high / Too low
#       4. break when correct
#       5. stop after MAX_ATTEMPTS and reveal the secret

import random

secret = random.randint(1, 20)
attempts = 0
MAX_ATTEMPTS = 5

while attempts < MAX_ATTEMPTS:
    attempts += 1
    user = int(input("Enter number: "))
    if user == secret:
        print("Guessed it")
        break
    else:
        if user > secret:
            print("Too high")
        else:
            print("Too low")
else: 
    print(f"Attempts exceeded the number was {secret}")