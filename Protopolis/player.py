# Player

import dice
import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.Crossbow()]

        self.hp = 100
        self.weapon = None
        self.unarmed_strike = dice.d4.roll()
        self.x = 1
        self.y = 2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def is_alive(self):
        self.hp > 0

    def print_inventory(self):
        print('Currently equipped weapon:\n', '*', str(self.weapon))
        print('Inventory:')
        for item in self.inventory:
            print('*', str(item))

    def examine_item(self, item):
        print(str(item), ':', item.description)
        print('Damage:', str(item.min_dmg), '-', str(item.max_dmg))
        print('Durability:', item.uses)
        if item.is_ranged():
            print('Type: Ranged')
        else:
            print('Type: Melee')

    def equip_weapon(self, item):
        self.weapon = item

    def attack(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        if self.weapon == None:
            print("You punch {}!".format(enemy.name))
            enemy.hp -= self.unarmed_strike
            if not enemy.is_alive():
                print("You killed {} with your bare hands!".format(enemy.name))
            else:
                print("{} HP is {}.".format(enemy.name, enemy.hp))
        else:
            print("You use {} against {}!".format(self.weapon, enemy.name))
            enemy.hp -= self.weapon.damage
            if not enemy.is_alive():
                print("You killed {}!".format(enemy.name))
            else:
                print("{} HP is {}.".format(enemy.name, enemy.hp))
# Test inventory
'''user = Player()

user.print_inventory()

user.equip_weapon(items.Crossbow())

user.print_inventory()'''

# Test examine_item
'''user = Player()

user.examine_item(user.inventory[2])
user.examine_item(user.inventory[0])
user.examine_item(user.inventory[1])'''
