# Connor Finley
# Advanced Python
# Assignment 02 - Inventory
# Date: 2017/09/04


def displayInventory(inventory):
  print("Inventory:")
  for item in inventory:
    print(inventory[item], item)
  total = sum(inventory.values())
  print("Total number of items:", total)
  

def addToInventory(inventory, addedItems):
  for addedItem in addedItems:
    if addedItem in inventory:
      inventory[addedItem] += 1
    else:
      inventory[addedItem] = 1
  return inventory
      

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)