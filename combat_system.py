import random
import time

player_list = range(1, 10)
enemy_list = range(1, 6)

PHP = 10
EHP = 5

while PHP > 0 or EHP > 0:
    player_attack = random.choice(player_list)
    enemy_attack = random.choice(enemy_list)

    player_defense = random.choice(player_list)
    enemy_defense = random.choice(enemy_list)

    if player_attack > enemy_defense:
        print("You have struck your foe.")
        EHP = EHP - 1
    else:
        print("Your enemy blocked your attack.")

    if EHP == 0:
        print("Your enemy has died.")
        break

    if enemy_attack > player_defense:
        print("Your foe struck you.")
        PHP = PHP - 1
    else:
        print("You blocked your enemy's attack.")

    if PHP == 0:
        print("You died.")
        break

    print("HP: ", PHP)
    time.sleep(3)

