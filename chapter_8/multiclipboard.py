#!/usr/bin/env python3
# Extending the Multiclipboard
# Saves and loads pieces of text to the clipboard.
# Usage: py.exe multiclipboard.py save <keyword> - Saves clipboard to keyword.
#        py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe multiclipboard.py list - Loads all keywords to clipboard.
#        py.exe multiclipboard.py delete <keyword> - Deletes keyword.
#        py.exe multiclipboard.py delete - Deletes all keywords.

import shelve
import pyperclip
import sys

shelf = shelve.open("multiclipboard")
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        # Save clipboard content.
        shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        # Delete keyword.
        del shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(shelf.keys())))
    elif sys.argv[1].lower() == "delete":
        # Delete all keywords.
        shelf.clear()
    elif sys.argv[1] in shelf:
        pyperclip.copy(shelf[sys.argv[1]])
shelf.close()
