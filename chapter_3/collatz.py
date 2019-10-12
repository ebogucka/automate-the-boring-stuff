#!/usr/bin/env python3
# The Collatz Sequence


def collatz(number):
    if number < 1:
        raise ValueError(f"{number} is not a positive integer!")
    result = number // 2 if number % 2 == 0 else 3 * number + 1
    print(result)
    return result


while True:
    try:
        number = int(input("Enter number:\n"))
    except ValueError:
        print("You must enter an integer!")
        continue
    else:
        break

while number != 1:
    number = collatz(number)
