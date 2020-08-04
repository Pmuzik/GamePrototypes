# Player

import items


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.Crossbow()]

        self.hp = 100
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
        print('Inventory:')
        for item in self.inventory:
            print('*', str(item))

    def examine_item(self, item):
        print(str(item), ':', item.description)
        print('Damage:', str(item.min_dmg), '-', str(item.max_dmg))
        print('Durability:', item.uses)
        if item.is_ranged() == True:
            print('Type: Ranged')
        else:
            print('Type: Melee')

# Test inventory
'''user = Player()

user.print_inventory()'''

# Test examine_item
'''user = Player()

user.examine_item(user.inventory[2])
user.examine_item(user.inventory[0])
user.examine_item(user.inventory[1])'''
