import time
import cmd
import sys
import os
from items_list import sword, axe, laser, chainsaw, rapier
#CnD_MINI_game
from Characters import Player, Enemy
import Dice
import random
from speech import speechText
import gauntlet
#from coloredText import colors





character_created = False
#game does not start until player creates a character

#Title Screen
def title_screen():

        os.system('cls')
        print(open('resources/title.txt').read())
        time.sleep(2)
        print()
        print("Press 'ENTER' to continue")
        input()
        os.system('cls')
#########################################################
def start_menu():

        os.system('cls')
        print('     -[S]tart-               \n     -[H]elp-                \n     -[Q]uit-                ')
        print()
        command = str.lower(input('\n> '))
        if command == 'start' or command == 's':
                character_creation()
        elif command == 'help' or command == 'h':
                help_menu()
        elif command == 'quit' or command == 'q':
                exit()

        while command not in ['start', 's', 'help', 'h', 'quit', 'q']:
                print("Please enter a valid command")
                command = str.lower(input('\n> '))
                if command == 'start' or command == 's':
                        character_creation()
                elif command == 'help' or command == 'h':
                        help_menu()
                elif command == 'quit' or command == 'q':
                        exit()

def help_menu():
        os.system('cls')
        speechText("""Welcome to Coffee & Donuts: MINI adventure! In this game
you will be frequently prompted to enter text commands. '>' Means 
you are being prompted to enter a command. Simply type one
of the suggested commands or the first letter of the command which is
indicated by '[]'. Commands are NOT case-sensitive--so don't worry!
""",0.04)
        print('\n')
        speechText('Good luck and have fun!',0.04)
        print('\n')
        speechText('-Adventure Solutions Inc., Management',0.04)
        print('\n')
        print("Press 'ENTER' to return to the main menu.")
        input()
        start_menu()




#Character Creation
##########################################################
def character_creation():
        #Collect player input
        os.system('cls')
        speechText('What is your name? ',0.04)
        player_name = input('\n> ')
        player.name = player_name
        os.system('cls')
        speechText('How do you like your coffee?', 0.04)
        print("""\n[1]: Black.
                \n[2]: Black as night and as sweet as the Devil.
                \n[3]: With cream and sugar.
                \n[4]: With a lot of milk. Basically coffee-flavored milk.""")
        coffee_choice = input('\n> ')
        if coffee_choice == '1':
                player.hp = 500
                player.max_hp = 500
                player.mp = 500
                player.max_mp = 500
                player.abilities = {}
                player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                "fire": {"Power":range(15, 25), "MP Cost": 10}}
                player.white_magic ={}

        elif coffee_choice == '2':
                player.hp = 1000
                player.max_hp = 1000
                player.mp = 1000
                player.max_mp = 1000
                player.abilities = {}
                player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                "firaga": {"Power":range(26, 70), "MP Cost": 30}}
                player.white_magic ={}

        elif coffee_choice == '3':
                player.hp = 500
                player.max_hp = 500
                player.mp = 2000
                player.max_mp = 2000
                player.abilities = {}
                player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                "firaga": {"Power":range(26, 70), "MP Cost": 30},
                                                "flare": {"Power": range(50, 100), "MP Cost": 50}}
                player.white_magic ={}

        elif coffee_choice == '4':
                player.hp = 5000
                player.max_hp = 5000
                player.mp = 500
                player.max_mp = 500
                player.abilities = {}
                player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                "firaga": {"Power":range(26, 70), "MP Cost": 30}}
                player.white_magic ={"curaga": {"Power": range(55, 150), "MP Cost": 55}}

        while coffee_choice not in ['1','2','3','4']:
                print('Please enter a valid command.')
                coffee_choice = input('\n> ')
                if coffee_choice == '1':
                        player.hp = 500
                        player.max_hp = 500
                        player.mp = 500
                        player.max_mp = 500
                        player.abilities = {}
                        player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                        "fire": {"Power":range(15, 25), "MP Cost": 10}}
                        player.white_magic ={}

                elif coffee_choice == '2':
                        player.hp = 1000
                        player.max_hp = 1000
                        player.mp = 1000
                        player.max_mp = 1000
                        player.abilities = {}
                        player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                                "firaga": {"Power":range(26, 70), "MP Cost": 30}}
                        player.white_magic ={}

                elif coffee_choice == '3':
                        player.hp = 500
                        player.max_hp = 500
                        player.mp = 2000
                        player.max_mp = 2000
                        player.abilities = {}
                        player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                        "firaga": {"Power":range(26, 70), "MP Cost": 30},
                                                        "flare": {"Power": range(50, 100), "MP Cost": 50}}
                        player.white_magic ={}

                elif coffee_choice == '4':
                        player.hp = 5000
                        player.max_hp = 5000
                        player.mp = 500
                        player.max_mp = 500
                        player.abilities = {}
                        player.black_magic ={"strike":{"Power": range(1,10), "MP Cost": 0}, 
                                                        "firaga": {"Power":range(26, 70), "MP Cost": 30}}
                        player.white_magic ={"curaga": {"Power": range(55, 150), "MP Cost": 55}}

        os.system('cls')
        speechText('What is your favorite type of donut?',0.04)
        print("""\n[1] Plain
                \n[2] Chocolate-Frosted
                \n[3] Jelly-Filled
                \n[4] Bavarian Creme
                \n[5] French Cruller""")
        donut_choice = input('\n> ')
        if donut_choice == '1':
                player.inventory.update(sword)

        elif donut_choice == '2':
                player.inventory.update(axe)

        elif donut_choice == '3':
                player.inventory.update(laser)

        elif donut_choice == '4':
                player.inventory.update(chainsaw)

        elif donut_choice == '5':
                player.inventory.update(rapier)

        while donut_choice not in ['1','2', '3', '4', '5']:
                print("Please enter a valid command.")
                donut_choice = input('\n> ')
                if donut_choice == '1':
                        player.inventory.update(sword)

                elif donut_choice == '2':
                        player.inventory.update(axe)

                elif donut_choice == '3':
                        player.inventory.update(laser)

                elif donut_choice == '4':
                        player.inventory.update(chainsaw)

                elif donut_choice == '5':
                        player.inventory.update(rapier)

        print("\nThis is your character.")
        print("\n")
        player.check_player_status()
        print('\n')
        print('\nYou are equipped with...')
        player.check_player_inventory()
        print('\n')
        print('Is this the character you want to use? ([y]es, [n]o)')
        answer = str.lower(input('\n> '))
        if answer == 'yes' or answer == 'y':
                character_created = True
        elif answer == 'no' or answer == 'n':
                print ('Start over?')
                answer2 = str.lower(input('\n> '))
                if answer2 == 'yes' or answer2 == 'y':
                        character_creation()
                elif answer2 == 'no' or answer2 == 'n':
                        start_menu()
                while answer2 not in ['yes', 'y', 'no', 'n']:
                        print('Please enter a valid command.')
                        answer2 = str.lower(input('\n> '))
                        if answer2 == 'yes' or answer2 == 'y':
                                character_creation()
                        elif answer2 == 'no' or answer2 == 'n':
                                start_menu()

        while answer not in ['yes', 'y', 'no', 'n']:
                        print('Please enter a valid command.')
                        answer = str.lower(input('\n> '))
                        if answer == 'yes' or answer == 'y':
                                character_created = True
                        elif answer == 'no' or answer == 'n':
                                print ('Start over?')
                                answer2 = str.lower(input('\n> '))
                                if answer2 == 'yes' or answer2 == 'y':
                                        character_creation()
                                elif answer2 == 'no' or answer2 == 'n':
                                        start_menu()
                                while answer2 not in ['yes', 'y', 'no', 'n']:
                                        print('Please enter a valid command.')
                                        answer2 = str.lower(input('\n> '))
                                        if answer2 == 'yes' or answer2 == 'y':
                                                character_creation()
                                        elif answer2 == 'no' or answer2 == 'n':
                                                start_menu()

##########################################################

#the gauntlet
##########################################################
def the_arena():
        while True:

                speechText('Are you ready to enter the arena? ([y]es, [n]o, [c]heck stats)', 0.04)
                enter_arena = input('\n> ')
                if enter_arena == 'yes' or enter_arena == 'y':
                        gauntlet.randomEncounter(player)
                elif enter_arena == 'no' or enter_arena == 'n':
                        print("\nYou retire.")
                        print("\nYou were...")
                        print(player)
                        player.check_player_inventory()
                        print("You defeated " + str(player.enemies_defeated) + " enemies.")
                        time.sleep(2)
                        print("Press 'ENTER' to return to start menu.")
                        input()
                        start_menu()
                elif enter_arena == 'check stats' or enter_arena == 'c':
                        print(player)
                        player.check_player_status()
                        player.check_player_inventory()
                        print("Press 'ENTER' to continue.")
                        input()
                        the_arena()
                while enter_arena not in ['yes', 'y', 'no', 'n', 'check stats', 'c']:
                        print('Please enter a valid command.')
                        enter_arena = input('\n> ')
                        if enter_arena == 'yes' or enter_arena == 'y':
                                gauntlet.randomEncounter(player)
                        elif enter_arena == 'no' or enter_arena == 'n':
                                print("\nYou retire.")
                                print("\nYou were...")
                                print(player)
                                player.check_player_inventory()
                                print("You defeated " + str(player.enemies_defeated) + " enemies.")
                                time.sleep(2)
                                print("Press 'ENTER' to return to start menu.")
                                input()
                                start_menu()
                        elif enter_arena == 'check stats' or enter_arena == 'c':
                                print(player)
                                player.check_player_status()
                                player.check_player_inventory()
                                print("Press 'ENTER' to continue.")
                                input()
                                the_arena()

########################################################
player = Player()
#creates instance of player

title_screen()
start_menu()

the_arena()
