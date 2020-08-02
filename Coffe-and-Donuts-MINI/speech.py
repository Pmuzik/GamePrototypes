import sys
import time
import textwrap


def speechText(txt, tme):
	txt = textwrap.fill(txt, width=70)
	for character in txt:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(tme)



#intro= 'Once upon a time... there was a cat who could travel through time and space.\
 #He saw many strange worlds and met many interesting people.'

#speechText(intro, 0.04)
