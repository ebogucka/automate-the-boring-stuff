#!/usr/bin/env python3
# Filling in the Gaps

import re
import os
import sys
import shutil

if len(sys.argv) < 2:
    print("Usage: filling_gaps.py <path>")
    sys.exit(1)

path = sys.argv[1]
regex = re.compile(r"(spam)(\d{3})(.txt)")
files = os.listdir(path)
files.sort()
next_name = "spam001.txt"
counter = 1
for filename in files:
    match = regex.match(filename)
    if match:
        if filename != next_name:
            print(f"Renaming {filename} => {next_name}")
            shutil.move(os.path.join(path, filename), os.path.join(path, next_name))
        counter += 1
        next_name = f"{match.group(1)}{counter:03}{match.group(3)}"
