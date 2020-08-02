#Dice
import random
class Die:
	'''Represents a single Die'''
	def __init__(self, sides=6):
		'''set the number of sides. Defaults to 6.'''
		self.sides = sides

	def roll(self):
		'''Roll the die'''
		return random.randint(1, self.sides)

Die()


D6 = Die()
D4 = Die(4)
D8 = Die(8)
D10 = Die(10)
D12 = Die(12)
D20 = Die(20)
D100 = Die(100)
#roll_result = D6.roll()
#print(roll_result)


