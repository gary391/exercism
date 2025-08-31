"""Functions to keep track and alter inventory."""
"""
dict() (the constructor for the dictionary class) 
can be used with any iterable of key, value pairs or with a series of <name>=<value> arguments:

#Passing a list of key,value tuples.

Accessing an entry via the .get(<key>, <default value>) method can avoid the KeyError:
bear.get("color", 'not found')
'not found'
"""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for item in items:
        # print(item)
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


# print(create_inventory(["coal", "coal", "coal", "coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    pass


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


# print(decrement_items({"coal": 2, "wood": 1, "diamond": 2}, ["coal", "coal", "wood", "wood", "diamond"]))
# print(decrement_items({"iron": 3, "gold": 2}, ["iron", "wood", "iron", "diamond"]))


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)
    return inventory


print(remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood"))


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_of_tuples = []
    for k,v in inventory.items():
        if v > 0:
        list_of_tuples.append((k, v))
    return list_of_tuples

print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))

