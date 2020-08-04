# Creating the world and maps for the game
# Reformat intro text to fit speech module
import random
import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
    def intro_text(self):
        return '''
    You find yourself in the ruins of what appears to be the promenade of one of the
    old underground commercial districts. The gaping hole in the ceiling and the soreness of your
    backside jogs a vague memory of how you got here.\n
    The dull yellow light of a broken glow-globe flickers in the distance beneath the rubble. 
    You can make out four paths, each as dark and foreboding as the next
    '''


class BoringTile(MapTile):
    def intro_text(self):
        return '''
    There does not appear to be much of interest in this part of the city--
    nothing but dusty ancient fragments of barely legible runes, frayed wiring,
    and corroded steel plating.
                   '''


class VictoryTile(MapTile):
    def intro_text(self):
        return '''
    You have found the Golden Gates of Protopolis!
    You step gingerly beneath the gaze of the bronze colossi who stand sentinel
    over the path. If they notice your passing, they give no indication.
    It seems you are free of the dangers of this place. 
    
    Thanks for playing!
    '''


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
        elif r < 0.80:
            self.enemy = enemies.Ogre()
        elif r < 0.95:
            self.enemy = enemies.BatColony()
        else:
            self.enemy = enemies.ChromeBeast()

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}.".format(self.enemy.name)

# Test map 1
world_map = [
    [None, VictoryTile(1,0), None],
    [None, EnemyTile(1,1), None],
    [BoringTile(0,2), StartTile(1,2), BoringTile(2,2)],
    [None, BoringTile(1,3), None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None

    try:
        return world_map [y][x]
    except IndexError:
        return None