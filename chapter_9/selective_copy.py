#!/usr/bin/env python3
# Selective Copy


import argparse
import shutil
import os

parser = argparse.ArgumentParser(
    description=(
        "Walks through a folder tree, searches for files with a given extension "
        "and copies them to a selected folder"
    )
)
parser.add_argument("path", type=str, help="directory tree to copy from")
parser.add_argument("extension", type=str, help="type of files to copy, e.g. txt")
parser.add_argument(
    "--out", type=str, default="./copy", help="directory to copy the files to"
)

args = parser.parse_args()

extension = args.extension
if not extension.startswith("."):
    extension = f".{extension}"

os.makedirs(args.out, exist_ok=True)
for folder, subfolders, files in os.walk(args.path):
    for file in files:
        if os.path.abspath(folder) == os.path.abspath(args.out):
            continue
        if file.endswith(extension):
            filename = os.path.join(folder, file)
            print(f"Copying {filename}...")
            shutil.copy(filename, args.out)
