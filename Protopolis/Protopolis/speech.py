import sys
import time
import textwrap


def speech_text(txt, tme):
    txt = textwrap.fill(txt, width=70)
    for character in txt:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(tme)


# Test speechText
'''intro = 'Once upon a time... there was a cat who could travel through time' \
        ' and space. He saw many strange worlds and met many interesting people.'

speech_text(intro, 0.04)'''