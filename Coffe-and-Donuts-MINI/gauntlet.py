#gauntlet
import random
import time
from Characters import Player, Enemy
from items_list import sword, axe, rapier, laser, chainsaw
from battle_system import battle
from enemy_list import e_dict

def recover_healthMP(self, amount):
        if self.hp + amount > self.max_hp:
                self.hp = self.max_hp
        else:
                self.hp += amount

        if self.mp + amount > self.max_mp:
                self.mp = self.max_mp
        else:
                self.mp += amount

def eat_donut(player):
        amount = random.randint(10, 999)
        recover_healthMP(player, amount)
        print('You have recovered ' + str(amount) + ' HP and '+ str(amount)+ ' MP.')
        print('Your total HP is ' + str(player.hp) + ' out of ' + str(player.max_hp) + '.')
        print('Your total MP is ' + str(player.mp)+ ' out of ' + str(player.max_mp) + '.')

def randomEncounter(player):
        encounter = random.randint(1,20)
        if encounter == 1:
                print('Someone from the stands tosses you a donut! Yummy!')
                eat_donut(player)
        elif encounter in range(2, 11):
            enemy = random.choice(e_dict['common'])
            battle(player, enemy)
            enemy.hp = enemy.max_hp
            enemy.mp = enemy.max_mp
        elif encounter in range(12, 18):
            enemy = random.choice(e_dict['uncommon'])
            battle(player, enemy)
            enemy.hp = enemy.max_hp
            enemy.mp = enemy.max_mp
        elif encounter in range(19,20):
            enemy = random.choice(e_dict['rare'])
            battle(player, enemy)
            enemy.hp = enemy.max_hp
            enemy.mp = enemy.max_mp
