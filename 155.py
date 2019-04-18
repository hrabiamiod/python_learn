
stuff = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzala': 12}

def displayInventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+k)
        item_total = item_total + v
    print("Całkowita liczba przedmiotów: " + str(item_total))


displayInventory(stuff)

