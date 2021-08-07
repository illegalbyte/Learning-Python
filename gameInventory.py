# Exercise from https://automatetheboringstuff.com/2e/chapter5/


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		# FILL THIS PART IN
		print(str(v) + " " + str(k))
		item_total += v

	print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
	