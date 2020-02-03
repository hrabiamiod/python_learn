import random

class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(60, 70)
enemy1.getAtk()

enemy1 = Enemy(160, 270)
enemy1.getAtk()

'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strike for", dmg, "points of damage. Current HP:", playerhp)

    if playerhp > 30:
        continue

    print("Moving to hospital...")
    break
    
'''