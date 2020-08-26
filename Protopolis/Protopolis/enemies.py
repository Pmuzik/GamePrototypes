import dice

d6 = dice.Die()
d4 = dice.Die(4)
d8 = dice.Die(8)
d10 = dice.Die(10)
d12 = dice.Die(12)
d20 = dice.Die(20)
d100 = dice.Die(100)

# enemies


class Enemy:
    def __init__(self):
        raise NotImplementedError('Do not create raw Enemy objects.')

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = 'Giant Spider'
        self.hp = 10
        self.damage = d6.roll()


class Ogre(Enemy):
    def __init__(self):
        self.name = 'Ogre'
        self.hp = 30
        self.damage = d10.roll()


class BatColony(Enemy):
    def __init__(self):
        self.name = 'Colony of Bats'
        self.hp = 75
        self.damage = d4.roll()


class ChromeBeast(Enemy):
    def __init__(self):
        self.name = 'Chrome-Beast'
        self.hp = 80
        self.damage = d6.roll() + 1


class GunDrone(Enemy):
    def __init__(self):
        self.name = 'Gun Drone'
        self.hp = 55
        self.damage = d4.roll() + 1