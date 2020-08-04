# Items

import dice

d6 = dice.Die()
d4 = dice.Die(4)
d8 = dice.Die(8)
d10 = dice.Die(10)
d12 = dice.Die(12)
d20 = dice.Die(20)
d100 = dice.Die(100)

# Weapons

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return self.name

    def is_ranged(self):
        return False

    def is_broken(self):
        return self.uses > 0


class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.description = 'A fist-sized rock, suitable for bludgeoning.'
        self.damage = d4.roll()
        self.min_dmg = 1
        self.max_dmg = 4
        self.uses = 100

class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.description = 'A small dagger, good for cutting and stabbing.'\
                           'Somewhat more dangerous than a rock.'
        self.damage = d6.roll()
        self.min_dmg = 1
        self.max_dmg = 6
        self.uses = 50

class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty Sword'
        self.description = 'An old blade found in the ruins.'\
                           'Perhaps a skilled smith can refurbish it.'
        self.damage = d6.roll() +1
        self.min_dmg = 2
        self.max_dmg = 7
        self.uses = 90

class BeamSaber(Weapon):
    def __init__(self):
        self.name = 'Beam Saber'
        self.description = 'Crafted from the technology of the Giants.'\
                           'A silver hilt which emits a green laser-beam.'
        self.damage = d10.roll()
        self.min = 1
        self.max.dmg = 10
        self.uses = 75

class Crossbow(Weapon):
    def __init__(self):
        self.name = 'Crossbow'
        self.description = 'A ranged weapon commonly found in the Western Kingdoms'
        self.damage = d6.roll()
        self.min_dmg = 1
        self.max_dmg = 6
        self.uses = 50

    def is_ranged(self):
        return True

class PlasmaRifle(Weapon):
    def __init__(self):
        self.name = 'Plasma Rifle'
        self.description = "A gun crafted from the Giants's technology."\
                           'Fires blue bolts of energy.'
        self.damage = d10.roll()
        self.min_dmg = 1
        self.max_dmg = 10
        self.uses = 75

    def is_ranged(self):
        return True