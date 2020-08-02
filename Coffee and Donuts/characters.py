#player

from abilities import ability, Spell
from spell_list import Fire, Bolt, Blizzard
from ability_list import Strike, Kick, Mocking_Dance, Axe_Swing, Horn

class character:
        def __init__(self, name, hp, maxHP, mp, maxMP, abilityList, spellList):
                self.name = name
                self.hp = hp
                self.maxHP = maxHP
                self.mp = mp
                self.maxMP = maxMP
                self.abilityList = abilityList
                self.spellList = spellList

        def is_alive(self):
                return self.hp > 0


        def attack(self, other):
                raise NotImplementedError

class Player(character):
        def __init__(self, name='Jo', hp=100, maxHP=100, mp=50, maxMP=50, abilityList=[Strike], spellList=[]):
                        super().__init__(name, hp, maxHP, mp, maxMP, abilityList, spellList)


        def is_alive(self):
                return self.hp > 0


        def attack(self, other):
                while True:
                        print()
                        choice = str(input("\nWhat move would you like to make?"))

            
                        if choice in self.abilityList:
                                damage = int(random.choice(self.abilityList[choice.dmg]))
                                other.hp -= damage
                                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                                break
                        if choice in self.spellList:
                                        damage = int(random.choice(self.spellList[choice.dmg]))
                                        other.hp -= damage
                                        print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                        else:
                                print("Not a valid move, try again!")

        def check_Abilities(self):
                print("=====\n    Abilities\n=====")
                for ability in self.abilityList:
                                print (ability.name)

        def check_Spells(self):
                print("=====\n    Spells\n=====")
                for spell in self.spellList:
                                print(spell.name)

        def class_choice():
                print('Are you a [F]ighter, [M]age, or [C]leric')
                player_class = str.lower(input('\n> '))
                if player_class == 'mage' or player_class == 'm':
                    player = Mage()
                    player.name = input('\nWhat is your name?\n> ')
                if player_class == 'fighter' or player_class == 'f':
                    player = Fighter()
                    player.name = input('\nWhat is your name?\n> ')

class Mage(Player):
        def __init__(self, name= '', hp=500, maxHP=500, mp=1000, maxMP=1000,
                                        abilityList= [Strike], spellList=[Fire, Bolt, Blizzard]):
                super().__init__(name, hp, maxHP, mp, maxMP, abilityList, spellList)

        def __str__(self):
                    return "{}\n=====\nHP:{}/{}\nMP:{}/{}".format(self.name, self.hp, self.maxHP, self.mp, self.maxMP)

class Fighter(Player):
        def __init__(self, name= '', hp=1000, maxHP=1000, mp=150, maxMP=150,
                                        abilityList= [Strike, Kick], spellList=[]):
                super().__init__(name, hp, maxHP, mp, maxMP, abilityList, spellList)

        def __str__(self):
                    return "{}\n=====\nHP:{}/{}\nMP:{}/{}".format(self.name, self.hp, self.maxHP, self.mp, self.maxMP)


class Enemy(character):
        def __init__(self, name, hp, maxHP, mp, maxMP, abilityList, spellList):
                super().__init__(name, hp, maxHP, mp, maxMP, abilityList, spellList)
        
        def attack(self, other):
                        cpu_choice = random.choice(list(self.abilityList))
                        if cpu_choice in self.abilityList:
                                        damage = int(random.choice(self.abilityList[cpu_choice]))
                                        other.health -= damage
                                        print("\nThe {2.name} attacks with {0}, dealing {1} damage.".format(cpu_choice, damage, self))
                        if cpu_choice in self.spellList:
                                        damage = int(random.choice(self.spellList[cpu_choice]))
                                        other.health -= damage
                                        print("\nThe {2.name} attacks with {0}, dealing {1} damage.".format(cpu_choice, damage, self))


enemy_list ={'common': [Enemy('Goblin', 30, 30, 30, 30, [Strike, Kick, Mocking_Dance], []), 
                                                Enemy('Orc', 100, 100, 25, 25, [Strike, Axe_Swing, Horn], [Fire])],
                }

def class_choice():
        print('Are you a [F]ighter, [M]age, or [C]leric')
        player_class = str.lower(input('\n> '))
        if player_class == 'mage' or player_class == 'm':
                self = Mage()
                self.name = input('\nWhat is your name?\n> ')
        if player_class == 'fighter' or player_class == 'f':
                self = Fighter()
                self.name = input('\nWhat is your name?\n> ')

#class_choice()

player= Player(name= 'Popo', hp=100, maxHP=100, mp=100, maxMP=100, abilityList=[Strike], spellList=[Fire])
print(player.name)
print(player.hp)
for ability in player.abilityList:
    print(ability.name)
player.check_Abilities()

player(name, )