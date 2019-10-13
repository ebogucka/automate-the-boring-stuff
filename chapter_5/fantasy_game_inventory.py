#!/usr/bin/env python3
# Fantasy Game Inventory


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(f"{value} {key}")
        item_total += value
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


stuff = {"gold coin": 42, "rope": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
stuff = add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
