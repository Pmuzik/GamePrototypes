#BattleArena
import random
import characters
from characters import class_choice, Player, Mage, Fighter
import time
from Dice import Die

def battle(player, enemy):

        print('The gates are open! A ferocious {0.name} strides into the arena! Prepare to fight!'.format(enemy))
        time.sleep(1)
        print('{0.name} has {0.hp}/{0.maxHP} HP and {0.mp}/{0.maxMP} MP.'.format(enemy))
        print('{0.name} has {0.hp}/{0.maxHP} HP and {0.mp}/{0.maxMP} MP.'.format(player))
        while player.hp > 0 and enemy.hp > 0:
                print('-------------------------------------------------')
                player.attack(enemy)
                if enemy.hp <= 0:
                    break
                print("\n{0.name}'s health is now {0.hp}/{0.maxHP}.".format(enemy))
                print('-------------------------------------------------')
                enemy.attack(player)
                if player.hp <= 0:
                    break
        print("\n{0.name}'s health is now {0.hp}/{0.maxHP}.".format(player))
            # outcome
        if player.hp > 0:
                print("You defeated {0.name}!".format(enemy))
        if enemy.hp > 0:
                print("You were defeated by {0.name}...".format(enemy))

def random_encouter():
        D100 = Die(100)
        encounter = D100.roll()
        if encounter in range(1,50):
                battle(player, random.choice(enemy_list['common']))
        elif encounter in range(51, 100):
                print('You wait patiently for the next challenger.')

def ready():
        answer = str.lower(input('\nAre you ready? \n>'))
        if answer == 'yes' or answer == 'y':
                random_encouter()
        if answer == 'no' or answer == 'n':
                print('You have had enough fighting for today.')

########################################################################################

#name= 'Jo', hp=10, maxHP=10, mp=10, maxMP=10, abilityList=[], spellList=[]
mage = Mage()
fighter = Fighter()
class_choice()


print(player.name)
player.check_Abilities()
player.check_Spells()



#while True:
#        ready()

