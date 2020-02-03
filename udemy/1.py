import random

playerhp = 200
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strike for", dmg, "points of damage. Current HP:", playerhp)

    if playerhp == 30:
        print("Moving to hospital...")
        break