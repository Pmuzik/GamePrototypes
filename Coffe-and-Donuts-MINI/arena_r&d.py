#arena_r&d
import random
import time
from Characters import Player, Enemy
from items_list import sword, axe, rapier, laser, chainsaw
from battle_system import battle

player = Player()
player.inventory.update(laser)
player.inventory.update(chainsaw)

goblin = Enemy('Goblin', 1000, 1000, 150, 150, {"strike":{"Damage": range(1,10), "MP Cost": 0}, "goblin-fire":{"Damage": range(25,35), "MP Cost": 70}}, {})

battle(player, goblin)

print(player.black_magic)
print('\n')
print(player.black_magic['strike'])
print('\n')
print(player.black_magic['strike']['Damage'])
print('\n')
print(player)
player.check_player_inventory()
