#!/usr/bin/env python3
# Strong Password Detection

import re


def check(password):
    lengthRegex = re.compile(r".{8,}")  # at least eight characters long
    if lengthRegex.search(password) is None:
        print("Password too short!")
        return

    lowerRegex = re.compile(r"[a-z]+")  # contains lowercase characters
    upperRegex = re.compile(r"[A-Z]+")  # contains uppercase characters
    if lowerRegex.search(password) is None or upperRegex.search(password) is None:
        print("Password should contain both lower and upper case characters!")
        return

    digitRegex = re.compile(r"[0-9]+")  # has at least one digit
    if digitRegex.search(password) is None:
        print("Password should contain at least one digit!")
        return

    print("That is a strong password!")


passwords = ["abc", "abcdefgh", "dA", "dfJHFcvcjhsdfmn", "dfJHFcvcjhsdfmn69"]
for password in passwords:
    print("\n" + password)
    check(password)
