#!/usr/bin/env python3
# Regex Search
# Usage: py.exe regex_search.py <directory> <regex>

import sys
import os
import re

if len(sys.argv) < 3:
    print("Usage: py.exe regex_search.py <directory> <regex>")
    sys.exit()

directory = sys.argv[1]
regex = sys.argv[2]

for filename in os.listdir(directory):
    if not filename.endswith(".txt"):
        continue

    with open(os.path.join(directory, filename)) as file:
        for line in file.readlines():
            if re.search(regex, line):
                print(f"Match in file {filename}:\n{line}")
