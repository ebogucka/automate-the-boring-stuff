#!/usr/bin/env python3
# Debuggin Coin Toss

import random

sides = ("heads", "tails")
guess = ""
while guess not in sides:
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.choice(sides)
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
