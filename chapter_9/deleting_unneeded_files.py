#!/usr/bin/env python3
# Deleting Unneeded Files
# Searches for files and folders that are >= 100MB.
# Usage: deleting_unneeded_files.py <path>

import sys
import os


def check_size(path):
    if os.path.getsize(path) >= 1e8:
        print(path)


if len(sys.argv) < 2:
    print("Usage: deleting_unneeded_files.py <path>")
    sys.exit(1)

path = sys.argv[1]
print("Large files and folders:")
for folder, subfolders, files in os.walk(path):
    for subfolder in subfolders:
        check_size(os.path.join(folder, subfolder))
    for file in files:
        check_size(os.path.join(folder, file))
