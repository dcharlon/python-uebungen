import sys
import random

while True:
    try:
        difficulty = input("level: ")
        if int(difficulty) > 0:
            break
        else:
            pass
    except ValueError:
        pass
rng_result = random.randint(1, int(difficulty))

while True:
    try:
        guess = input("Guess the number: ")
        if int(guess) < 1:
            pass
        elif int(guess) > rng_result:
            print("Too large! ")
        elif int(guess) < rng_result:
            print("Too small! ")
        else:
            sys.exit("Just right! ")
    except ValueError:
        pass