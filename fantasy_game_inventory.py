#!/usr/bin/python3

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        # ROWAN CODE IN THIS INDENT
        item_total += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(item_total))

display_inventory(stuff)

# List to Dictionary function for Fantasy Game Inventory


def add_to_inventory(inventory, added_items):
    # ROWAN CODE IN THIS INDENT
    # TODO

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
