#!/usr/bin/env python3
# Comma Code


def to_string(items):
    if not items:
        return ""
    if len(items) == 1:
        return items[-1]
    return ", ".join(items[:-1]) + ", and " + items[-1]
