#ability class
import random

class ability:
        def __init__(self, name, description, dmg):
                self.name = name
                self.description = description
                self.dmg = dmg

        def __str__(self):
                return "{}\n=====\n{}\nBase Damage: {}\n".format(self.name, self.description, self.dmg)

        def generate_damage(self):
                low = self.dmg - 15
                high = self.dmg + 15
                return random.range(low, high)

#Strike = ability('Strike', 'A basic unarmed strike.', 10)

class Spell(ability):
        def __init__(self, name, description, dmg, element, mpCost):
                super().__init__(name, description, dmg)
                self.element = element
                self.mpCost = mpCost

        def __str__(self):
                return "{}\n=====\n{}\nBase Damage: {}\nElement: {}\nMP: {}\n".format(self.name, self.description, self.dmg, self.element, self.mpCost)

        def spend_mp(self, other):
                other.mp =- self.mpCost
                if other.mp < 0:
                        other.mp = 0

#Example:
#Blizzard = Spell('Blizzard', 'A burst of ice-shards.', 150, 'ice', 25)
#Fire = Spell('Fire', 150, 'fire', 25)
#print(str(Fire.mpCost))

#print(Strike)
#print(Blizzard)