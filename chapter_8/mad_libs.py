#!/usr/bin/env python3
# Mad Libs
# Usage: py.exe mad_libs.py <file>

import sys
import re
import os

if len(sys.argv) < 2:
    print("Usage: py.exe mad_libs.py <file>")
    sys.exit()

filename = sys.argv[1]
parts_of_speech = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]
with open(filename) as file:
    text = file.read()

pattern = re.compile("|".join(parts_of_speech))
placeholders = pattern.findall(text)

for placeholder in placeholders:
    prompt = "Enter "
    prompt += "a" if placeholder.startswith("a") else "an"
    prompt += f" {placeholder.lower()}: "

    new_word = input(prompt)
    text = re.sub(pattern=placeholder, repl=new_word, string=text, count=1)

print(text)

name, extension = os.path.splitext(filename)
new_file = f"{name}_mad{extension}"
with open(new_file, "w") as file:
    file.write(text)
