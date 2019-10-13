#!/usr/bin/env python3
# Table Printer


def print_table(data):
    column_widths = [len(max(column, key=len)) for column in data]
    for row in range(len(data[0])):
        for column in range(len(data)):
            print(data[column][row].rjust(column_widths[column]), end=" ")
        print()


table_data = [
    ["apples", "oranges", "cherries", "banana", "blueberries"],
    ["Alice", "Bob", "Carol", "David", "Josh"],
    ["dogs", "cats", "moose", "goose", "crested gecko"],
]

print_table(table_data)
