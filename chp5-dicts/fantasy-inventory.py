stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(stuff):
    print('Inventory')
    item_total = 0

    for k,v in stuff.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print ('Total: ' + str(item_total))

#displayInventory(stuff)

#List to dictionary
def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:
        currItem = inventory.get(i,0)
        currItem = currItem + 1
        inventory[str(i)] = currItem
        #print(inventory[str(i)])
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
