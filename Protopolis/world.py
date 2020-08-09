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
            self.alive_text = "A giant spider jumps down from " \
                "its web in front of you!"
            self.dead_text = "The corpse of a dead spider " \
                "rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre lies sprawled on the " \
                "ground before you."
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a series of shrill squeaks " \
                "getting closer... " \
                "Suddenly you are lost in a swarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.ChromeBeast()
            self.alive_text = "A Chrome-Beast bursts from a wall and " \
                "and bares its razor-sharp fangs at you!"
            self.dead_text = "A puddle of silvery liquid lies where the " \
                "Chrome-Beast once stood. It seems inert... for now."

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} does {} damage. You have {} HP remaining.".format(self.enemy.name,
                                                                        self.enemy.damage,
                                                                        player.hp))

# Test map 1
world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]


def tile_at(x, y):

    if x < 0 or y < 0:
        return None

    try:
        return world_map[y][x]
    except IndexError:
        return None
