#Characters
import random
from speech import speechText


class character:
        """base class for all characters"""
        def __init__(self, name, hp, max_hp, mp, max_mp, abilities, inventory):
                """Creates new character
                param name: name of the character
                param hp: character's hit points
                param max_hp: maximum number of hit points a character can have
                param mp: magic points for casting magic
                param max_mp: maximum number of magic points a character can have
                param str: character's Strength stat
                param defn: character's Defense stat
                param agi: character's Agility stat
                param mana: character's Mana stat
                param exp: how much exp the character has
                param inventory: contains items
                param equipment: contains equipped items
                param status: track status effects such as poison or paralyze"""

                self.name = name
                self. hp = hp
                self.max_hp = max_hp
                self.mp = mp
                self.max_mp = max_mp
                self.abilities = abilities
                self.inventory = inventory

        def is_alive(self):
                return self.hp > 0

        def attack(self, other):
            raise NotImplementedError

class Player(character):
        def __init__(self, name="Jo", hp=1000, max_hp=1000, mp=1000, max_mp=1000, abilities={}, inventory={},
        	black_magic = {"fire": {"Power" :range(15, 25), "MP Cost": 10},"strike":{"Power": range(1,10), "MP Cost": 0}},
        	white_magic = {"curaga": {"Power": range(55, 150), "MP Cost": 55}}, victory=False, enemies_defeated=0):
                                super().__init__(name, hp, max_hp, mp, max_mp, abilities, inventory)

                                self.name = "Jo"
                                self.hp = 1000
                                self.max_hp = 1000
                                self.mp = 1000
                                self.max_mp = 1000
                                self.inventory = {}
                                self.abilities =  {}
                                self.black_magic = {"fire": {"Power" :range(15, 25), "MP Cost": 10},"strike":{"Power": range(1,10), "MP Cost": 0}} 
                                self.white_magic = {"curaga": {"Power": range(55, 150), "MP Cost": 55}}
                                                                                                  
                                                    
                                self.victory = False
                                self.enemies_defeated = 0

        def __str__(self):
                        return "{}\n=====\nHP: {}/{}\nMP: {}/{}".format(self.name, self.hp, self.max_hp, self.mp, self.max_mp)

        def check_player_status(self):


                        print(self)
                        print("=====\n  Abilities\n=====")
                        for x in self.abilities:
                                print (x)
                                for y in self.abilities[x]:
                                        print (y, ':', self.abilities[x][y])
                        
                        print("=====\n  Black Magic\n=====")
                        for x in self.black_magic:
                                print (x)
                                for y in self.black_magic[x]:
                                        print (y, ':', self.black_magic[x][y])
                        
                        print("=====\n  White Magic\n=====")
                        for x in self.white_magic:
                                print (x)
                                for y in self.white_magic[x]:
                                        print (y, ':', self.white_magic[x][y])



        def check_player_inventory(self):
            print("=====\n  Inventory\n=====")
            for x in self.inventory:
                print(x)
                for y in self.inventory[x]:
                    print (y, ':', self.inventory[x][y])

        def attack(self, other):
                while True:
                    choice = str.lower(input("\nWhat move would you like to make? (type the name of the ability or item you want to use.)"))
                    if choice in self.black_magic:
                        if self.mp < self.black_magic[choice]['MP Cost']:
                                print('You do not have enough MP to cast that.')
                        elif self.mp >= self.black_magic[choice]['MP Cost']:
                                mp_cost = int(self.black_magic[choice]['MP Cost'])
                                self.mp -= mp_cost
                                damage = int(random.choice(self.black_magic[choice]['Power']))
                                other.hp -= damage
                                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                                break

                    elif choice in self.white_magic:
                        if self.mp < self.white_magic[choice]['MP Cost']:
                                print('You do not have enough MP to cast that.')
                        elif self.mp >= self.white_magic[choice]['MP Cost']:
                                mp_cost = int(self.white_magic[choice]['MP Cost'])
                                self.mp -= mp_cost
                                heal = int(random.choice(self.white_magic[choice]['Power']))
                                self.hp += heal
                                if self.hp > self.max_hp:
                                	self.hp = self.max_hp
                                print("\nYou heal with {0}, recovering {1} HP.".format(choice, heal))
                                break

                    elif choice in self.inventory:
                        if self.inventory[choice]['Uses'] <= 0:
                            print('You cannot attack with that! Your weapon is broken!')
                        else:
                            self.inventory[choice]['Uses'] -= 1
                            damage = int(random.choice(self.inventory[choice]['Power']))

                            other.hp -= damage
                            print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                            break
                    else:
                        print("Not a valid move, try again!")

class Enemy(character):
        def __init__(self, name, hp, max_hp, mp, max_mp, abilities, inventory):
                                #self.rate = rate
                                #self.description = description
                                super().__init__(name, hp, max_hp, mp, max_mp, abilities, inventory)
        
        def attack(self,other):
                cpu_choice = random.choice(list(self.abilities))
                if cpu_choice in self.abilities:
                        if self.mp < self.abilities[cpu_choice]['MP Cost']:
                                print("\nThe {} fumbles their attack.".format(self.name))
                        else:
                                mp_cost = int(self.abilities[cpu_choice]['MP Cost'])
                                self.mp -= mp_cost
                                damage = int(random.choice(self.abilities[cpu_choice]['Power']))
                                other.hp -= damage
                                print("\n {2.name} attacks with {0}, dealing {1} damage.".format(cpu_choice, damage, self))
