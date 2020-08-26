# Dice
import random


# represents a single die
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


d6 = Die()
d4 = Die(4)
d8 = Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)
d100 = Die(100)


# Test the dice
'''print('d6:',d6.roll())
print('d4:',d4.roll())
print('d10:',d10.roll())
print('d12:',d12.roll())
print('d20:',d20.roll())
print('d100:',d100.roll())'''