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


#D6 = Die()
#roll_result = D6.roll()
#print(roll_result)


