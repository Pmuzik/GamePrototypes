#battle module
import time
from Characters import Player, Enemy

def battle(player, enemy):
    print('You stumbled upon a {0.name}! Prepare to fight!'.format(enemy))
    time.sleep(1)
    print('{0.name} has {0.hp}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(enemy))
    print('{0.name} has {0.hp}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(player))
    while player.hp > 0 and enemy.hp > 0:
        print('--------------------------------------------------------------')
        player.check_player_status()
        player.check_player_inventory()
        print('--------------------------------------------------------------')
        player.attack(enemy)
        if enemy.hp <= 0:
            break
        print("\nThe health of the {0.name} is now {0.hp}/{0.max_hp}.".format(enemy))
        enemy.attack(player)
        if player.hp <= 0:
            break
        print("\n{0.name}'s' health is now {0.hp}/{0.max_hp}.".format(player))
    # outcome
    if player.hp > 0:
        player.enemies_defeated = player.enemies_defeated + 1
        print("You defeated the {0.name}!".format(enemy))
        
        
    if enemy.hp > 0:
        print("You were defeated by the {0.name}...".format(enemy))