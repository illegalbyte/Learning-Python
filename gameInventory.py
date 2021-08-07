# Exercise from https://automatetheboringstuff.com/2e/chapter5/
import copy

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		# FILL THIS PART IN
		print(str(v) + " " + str(k))
		item_total += v

	print("Total number of items: " + str(item_total), end='\n\n')

displayInventory(stuff)

def addToInventory(oldinventory, addedItems):
	newInventory = copy.deepcopy(oldinventory)
	for i in addedItems:
		for k, v in oldinventory.items():
			if k == i:
				v += 1
				newInventory[i] += 1
			else:
				newInventory.setdefault(i, 1)
	return newInventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)