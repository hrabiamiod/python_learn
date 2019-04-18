## Automate the Boring Stuff Chpt 5 - Fantasy Game Inventory ##

def displayInventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+k)
        item_total = item_total + v
    print("Całkowita liczba przedmiotów: " + str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) #sprawdzenie czy jest produkt, jesli nie to dodanie go z 0 stanem
        inventory[item] += 1 # pobranie nazwy na podstawie tego co zwróci pętla z item i dodanie +1
    return inventory

inv = {'złote monety': 1, 'lina': 3}

dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
