#battle module
import time
import Characters


def battle(player, enemy):
    print('You stumbled upon a {0.name}! Prepare to fight!'.format(enemy))
 #   time.sleep(1)
    print('{0.name} has {0.hp}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(enemy))
    print('{0.name} has {0.hp}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(player))
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print("\nThe health of the {0.name} is now {0.hp}/{0.max_hp}.".format(enemy))
        enemy.attack(player)
        if player.health <= 0:
            break
        print("\n{0.name}'s' health is now {0.hp}/{0.max_hp}.".format(player))
    # outcome
    if player.health > 0:
        print("You defeated the {0.name}!".format(enemy))
    if enemy.health > 0:
        print("You were defeated by the {0.name}...".format(enemy))