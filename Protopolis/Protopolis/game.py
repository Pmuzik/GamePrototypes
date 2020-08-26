from player import Player
import sys
import time
import os
import world
# import speech # This module isn't working well yet


def play():
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print('Go North')
            player.move_north()
        elif action_input in ['s', 'S']:
            print('Go South')
            player.move_south()
        elif action_input in ['e', 'E']:
            print('Go East')
            player.move_east()
        elif action_input in ['w', 'W']:
            print('Go West')
            player.move_west()
        elif action_input in ['i', 'I']:
            player.print_inventory()
        elif action_input in ['c', 'C']:
            check = input('Which item do you want to examine?\n>')
            for item in player.inventory:
                if check.capitalize() == item.name:
                    player.examine_item(item)
                else:
                    pass
        # TODO: equip weapon command
        elif action_input in ['a', 'A']:
            player.attack()
        elif action_input in ['q', 'Q']:
            exit()
        elif action_input in ['h', 'H']:
            print('''
                        Player Commands:\n
                        * N, n: Go North\n
                        * S, s: Go South\n
                        * E, e: Go East\n
                        * W, w: Go West\n
                        * A, a: Attack\n
                        * I, i: Display inventory\n
                        * C, c: Examine details of an item\n
                        * H, h: Help\n
                        * Q, q: Quit
                        ''')
        else:
            print('Invalid action!')

def get_player_command():
    return input('Action\n>')

def title_screen():
    # os.system('cls')
    print(open('assets/title.txt').read())
    print('\t\t\t\tEscape the City of Giants')
    time.sleep(2)
    print('\nPress ENTER to continue')
    input()
    os.system('cls')
    start_menu()


def start_menu():
    while True:
        user_in = input('[S]tart\n[Q]uit\n[H]elp\n>')
        if user_in.lower() == 's':
            play()
        elif user_in.lower() == 'q':
            exit()
        elif user_in.lower() == 'h':
            print('''
            Player Commands:\n
            * N, n: Go North\n
            * S, s: Go South\n
            * E, e: Go East\n
            * W, w: Go West\n
            * I, i: Display inventory\n
            * C, c: Examine details of an item\n
            * H, h: Help\n
            * Q, q: Quit
            ''')


title_screen()
