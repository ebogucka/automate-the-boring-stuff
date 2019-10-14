#!/usr/bin/env python3
# Regex Version of string.strip()

import re


def strip(s, chars=""):

    if not chars:
        regex = re.compile(r"^\s*|\s*$")
        return regex.sub("", s)

    regex = re.compile(f"^[{chars}]*|[{chars}]*$")
    return regex.sub("", s)
