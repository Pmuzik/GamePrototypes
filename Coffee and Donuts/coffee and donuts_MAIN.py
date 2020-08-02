#COFFEE & DONUTS

import random
import time
import cmd
import sys
import os
import textwrap

screen_width = 100

DONUTS = [8, 9, 10]
COFFEE = [1, 2, 3]
BANDERSNATCH = [4, 5, 6]
FAIRY = [7]
EXITLABYRINTH = [11]
TRAP = [12]
HERMIT = [13, 14]

KEYWORDS = ['fart','wander aimlessly', 'shout','open third eye', 'sleep', 'crit', 'perspective', 'fight', 'fire', 'go back',
'manager', 'ceo', 'conbini', 'inventory', 'wait']

MANAGER_SAYS =["...there's a secret weapon hidden down there, but you need to take the CRITical path to get there, meow.\n", 
"...there's a strange old hermit living in the company labyrinth. No idea how he got there but he must know some secrets to surviving down there, meow.\n",
"...getting out isn't the hard part. If you truly want to beat the labyrinth, meow, you need to hunt something dangerous, meow.\n",
"...the mad lads in R&D have been working on a new prototype, meow. It's been a pretty daunting project.\
Hopefully, after the beta testing is done, they'll have gained a fresh PERSPECTIVE, meow.\n",
"...using keywords will bump up your score but... not by much, meow.\n",
"...the company labyrinth is actually in some kind of pocket-dimension, meow. Very few things are fixed in place. The exit, for instance, will\
change if you walk away from it.\n"]

HERMIT_SAYS = ["The wise say, 'Don't FART'... or do they?\n", "The wise say, 'don't WANDER AIMLESSLY.'\n", "The wise do not SHOUT.\n", 
"Look within to look beyond... OPEN your THIRD EYE.\n", "Don't forget to SLEEP.\n", "Sometimes you must GO BACK to go forward.\n",
"What is the secret to my survival? Simple, I live next to a CONBINI.\n", "The wise often check their INVENTORY.\n", 
"The wise say, 'Good things come to those who WAIT...'\n", "The wise say, 'It is never too late to ask for help.'\n"]

moves = {"tackle": range(18, 26),
         "fire-bolt": range(10, 36),
         "heal": range(10, 20)}

omega_moves = {"tackle": range(30, 40),
                                "minigun": range(15, 35),
                                "chainsaw": range(1, 999)}


##useless dictionaries##
#damage = {'bandersnatch': range(10,15), 'trap':range(1,20)}
#heal = {'donut': range(10,15), 'coffee': range(5,20), 'fairy':range(5,100)}
#times_explored = 0


##### Player Setup #####
class character:
        def __init__(self, name, health, mp, max_hp, max_mp):
                self.name = name
                self.health = health
                self.mp = mp
                self.max_hp = max_hp
                self.max_mp = max_mp

        def attack(self, other):
                raise NotImplementedError

class player(character):
        def __init__(self, name= '', health= 100, mp= 100, max_hp= 200, max_mp= 200):
            super().__init__(name, health, mp, max_hp, max_mp)
            self.name = ''
            self.health = 100
            self.mp = 100
            self.game_on = True
            self.times_explored = 0
            self.max_hp = 200
            self.max_mp = 200
            self.keywords_used = 0
            self.inventory = {}
           #self.score = (self.hp + self.mp)*self.times_explored ##For some reason this keeps returning 0
        def attack(self, other):
                while True:
                        if 'OMEGA WEAPON' not in player.inventory:

                                choice = str.lower(input("\nWhat move would you like to make? (Tackle, Fire-bolt(5 MP), or Heal(10 MP))"))

                                if choice == "heal":
                                        self.health += int(random.choice(moves[choice]))
                                        if self.health > self.max_hp:
                                                self.health = self.max_hp
                                        else: 
                                                pass
                                        print("\nYour health is now {0.health}.".format(self))
                                        break
                                if choice == "tackle" or choice == "fire-bolt":
                                        damage = int(random.choice(moves[choice]))
                                        other.health -= damage
                                        print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                                        break
                                else:
                                        print("Not a valid move, try again!")

                        elif 'OMEGA WEAPON' in player.inventory:
                                choice = str.lower(input("\nWhat move would you like to make? (Tackle, Minigun, or Chainsaw)"))
                                if choice in ['tackle', 'minigun', 'chainsaw']:
                                        damage = int(random.choice(omega_moves[choice]))
                                        other.health -= damage
                                        print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                                        break
                                else:
                                        print("Not a valid move, try again!")

                        
#enemy character setup
class enemy(character):
        def __init__(self, name, health, mp, max_hp, max_mp):
                super().__init__(name, health, mp, max_hp, max_mp)
                
        def attack(self, other):
            if self.health <= 35:
                # increasing probability of heal when under 35 health, bit janky
                 moves_1 = ["tackle", "fire-bolt", "heal", "heal", "heal", "heal", "heal"]
                 cpu_choice = random.choice(moves_1)
            else:
                cpu_choice = random.choice(list(moves))
            if cpu_choice == "tackle" or cpu_choice == "fire-bolt":
                damage = int(random.choice(moves[cpu_choice]))
                other.health -= damage
                print("\nThe {2.name} attacks with {0}, dealing {1} damage.".format(cpu_choice, damage, self))
            if cpu_choice == "heal":
                self.health += int(random.choice(moves[cpu_choice]))
                if self.health > self.max_hp:
                        self.health = self.max_hp
                else: 
                        pass
                print("\nThe {0.name} uses heal and its health is now {0.health}.".format(self))

Enemies = {'common': [enemy('Goblin', 30, 30, 30, 30), enemy('Mindflayer', 50, 100, 50, 100)],
        'uncommon':[enemy('Wyrm', 150, 150, 150, 150)], 'rare':[enemy('Bandersnatch', 100, 50, 100, 50)],
        'secret': enemy('Xagor', 300, 300, 300, 300)}
###### Title Screen ######

def title_screen():    
                os.system('cls')
                print('################################')
                print('########COFFEE & DONUTS#########')
                print('################################')
                print('            -Start-             ')
                print('            -Help-              ')
                print('            -Quit-              ')
        
                option = input('\n> ')
                if option.lower() == ('start'):
                        intro()
                        setup_game()
                elif option.lower() == ('help'):
                        help_menu()
                elif option.lower() == ('skip'):
                        setup_game()
                elif option.lower() == ('quit'):
                        exit()
                while option.lower() not in ['start', 'help', 'quit', 'skip']:
                        print("Please enter a valid command.")
                        option = input('\n>')
                        if option.lower() == ('start'):
                                intro()
                                setup_game()
                        elif option.lower() == ('help'):
                                help_menu()
                        elif option.lower() == ('quit'):
                                exit()
####Explains gameplay#####
def help_menu():
        print('Enter "start" to start the game.\n Enter "skip" to start the game without the intro.\nYou will often be prompted to type "yes" or "no" or a keyword.\nA keyword will be printed in all CAPS.')
        print('You will start with 100 HP and 100 MP.\nIf your HP reaches 0 you will lose the game. You can use your MP to cast magic to avoid this.\nDo you understand?')
        understood = input('\n> ')
        if understood.lower() ==  ('yes') or understood.lower() == ('y'):
                title_screen()
        if understood.lower() == ('no') or understood.lower() == ('n'):
                print('Really? You seem to have a grasp of the basics.')
                time.sleep(2)
                title_screen()
        while understood.lower() not in ['yes', 'y', 'no', 'n']:
                        print('Just type "yes", "no", "y", or "n". Do you understand?')
                        understood = input('\n> ')
                        if understood.lower() ==  ('yes') or understood.lower() == ('y'):
                                title_screen()
                        if understood.lower() == ('no') or understood.lower() == ('n'):
                                print('Really? You seem to have a grasp of the basics.')
                                time.sleep(2)
                                title_screen()

####GAME FUNCTIONALITY####

def battle(player, enemy):
    print('You stumbled upon {0.name}! Prepare to fight!'.format(enemy))
    time.sleep(1)
    print('{0.name} has {0.health}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(enemy))
    print('{0.name} has {0.health}/{0.max_hp} HP and {0.mp}/{0.max_mp} MP.'.format(player))
    while player.health > 0 and enemy.health > 0:
        print('-------------------------------------------------')
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print("\n{0.name}'s health is now {0.health}/{0.max_hp}.".format(enemy))
        enemy.attack(player)
        if player.health <= 0:
            break
        print("\n{0.name}'s health is now {0.health}/{0.max_hp}.".format(player))
    # outcome
    if player.health > 0:
        print("You defeated {0.name}!".format(enemy))
    if enemy.health > 0:
        print("You were defeated by {0.name}...".format(enemy))

##HP/MP Recovery, damage, Max hp/mp check###

def check_health():
        if player.health <= 0:
                print('You died.')
                player.game_on = False
        else:
                pass

def recover_health(self, amount):
        if self.health + amount > self.max_hp:
                self.health = self.max_hp
        else:
                self.health += amount

def recover_MP(self, amount):
        if self.mp + amount > self.max_mp:
                self.mp = self.max_mp
        else:
                self.mp += amount

def damage(self, amount):
        if self.health - amount < 0:
                self.health = 0
        else:
                self.health -= amount
        check_health()

def spendMP(self, amount):
        if self.mp - amount < 0:
                self.mp = 0
        else:
                self.mp -= amount
        
def eat_donut():
        amount = random.randint(10, 20)
        recover_health(player, amount)
        print('You have recovered ' + str(amount) + ' HP.')
        print('Your total HP is ' + str(player.health) + ' out of ' + str(player.max_hp) + '.')

def drink_coffee():
        amount = random.randint(15, 25)
        recover_MP(player, amount)
        print('You have recovered ' + str(amount) + ' MP.')
        print('Your total MP is ' + str(player.mp) + ' out of ' + str(player.max_mp) + '.')

def fairy():
        amount = random.randint(1, 100)
        recover_health(player, amount)
        print('You have recovered ' + str(amount) + ' HP.')
        print('Your total HP is ' + str(player.health) + ' out of ' + str(player.max_hp) + '.')
        recover_MP(player, amount)
        print('You have recovered ' + str(amount) + ' MP.')
        print('Your total MP is ' + str(player.mp) + ' out of ' + str(player.max_mp) + '.')

def bandersnatch():
        amount = random.randint(10, 50)
        damage(player, amount)
        
def trap():
        amount = random.randint(1,30)
        damage(player,amount)
    
#defines how much MP is depleted by casting fire    
def fire():
        spendMP(player, 25)
        print('You spent 25 MP to cast FIRE.')
        print('You now have ' +str(player.mp)+' MP.')

###This function randomly selects a string from HERMIT_SAYS###
def list_random(HERMIT_SAYS):
    return HERMIT_SAYS[random.randint(0,len(HERMIT_SAYS)-1)]



####Choose whether or not you want to explore again (or do something else)
def explore():
        while player.game_on == True:
        
                
                explore1 = 'Do you wish to explore the labyrinth?\n'
                for character in explore1:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.03)
                response = input('> ')
                if response.lower() in KEYWORDS:
                    player.keywords_used = player.keywords_used + 1
                if response.lower() == ('yes') or response.lower() == ('y'):
                        roll_the_dice()
                elif response.lower() == ('no') or response.lower()==('n'):
                        bad_ending1 = 'You sit and wait for the manager cat to come rescue you.\n'
                        for character in bad_ending1:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.03)
                        break
                elif response.lower() == ('open third eye'):
                        third_eye = 'A third eye suddenly appears on your forehead allowing you to see the exit.\n'
                        for character in third_eye:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.03)
                        break
                elif response.lower() == ('shout'):
                        shout = 'The bandersnatch heard you and took you by surprise! It landed a critical hit and killed you!\n'
                        for character in shout:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.03)
                        player.health = 0
                        break
                
                elif response.lower() == ('wander aimlessly'):
                        if 'OMEGA WEAPON' not in player.inventory:
                               trap()
                               print('You walked into a wall and hurt your nose.')
                               print('You now have ' +str(player.health)+ ' HP.')
                        elif 'OMEGA WEAPON' in player.inventory:
                                print('You walk into a wall...')
                                time.sleep(2)
                                print('...and feel nothing because you are sitting in the sturdy, impenetrable frame of the Omega Weapon Mk. I.')

                elif response.lower() == ('fart'):
                        bsnatch = True
                        while bsnatch == True:
                                battack = 'You attract a bandersnatch with your farts!\n The bandersnatch lunges at you! Do you FIGHT back or cast FIRE?\n'
                                for character in battack:
                                        sys.stdout.write(character)
                                        sys.stdout.flush()
                                        time.sleep(0.03)
                                action = input('> ')
                                if action.lower() == 'fight':
                                        print("You got scratched up by the bandersnatch, but it's gone--for now...\n")
                                        bandersnatch()
                                        print("Your HP is " + str(player.health) +".")
                                        print("Your MP is " + str(player.mp) +".")
                                        bsnatch = False
                                if action.lower() == 'fire':
                                        fire()
                                        time.sleep(1)
                                        print("You drove off the bandersnatch with fire!\n")
                                        bsnatch = False
                                else:
                                        print("You can't do that now.")

                elif response.lower() == ('sleep'):
                        print('You sleep. And in your dreams you see a mysterious old hermit. He says to you...\n')
                       
                        time.sleep(2)
                        say = list_random(HERMIT_SAYS)
                        for character in say:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.05)

                elif response.lower() == ('go back'):
                        go_back = 'You trace your steps back to the labyrinth entrance and find a trap door that you did not notice before...\n'
                        for character in go_back:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.03)
                        print('Do you open it?')
                        response = input('> ')
                        if response.lower() == ('yes') or response.lower() == ('y'):
                                print('You have discovered the secret boss of the labyrinth--Xagor!')
                                xagor = '"Foolish mortal! You have disturbed my thousand-year slumber, and now you shall die!"'
                                for character in xagor:
                                        sys.stdout.write(character)
                                        sys.stdout.flush()
                                        time.sleep(0.04)
                                battle(player, Enemies['secret'])
                                check_health()
                        if response.lower() == ('no') or response.lower() == ('n'):
                                print('You feel an ominous presence lurking in the chamber below...')
                                time.sleep(2)
                                print('You decide to leave the trap door be.')
                elif response.lower() == ('perspective'):
                        if 'BLUEPRINT' in player.inventory:
                                print('There is naught but a rectangular outline in the dust where the blueprint once lay.')

                        if 'BLUEPRINT' not in player.inventory:
                                print('You find a blueprint for some kind of... machine?')
                                print('###########')
                                print('#   [A]   #')
                                print('# Mo-8-oM #')
                                print('#  | Y |  #')
                                print('# |w   w| #')
                                print('#  /   \\  #')
                                print('#OMEGA WPN#')
                                print('#MK.I     #')
                                print('###########') 
                                take = input('Take the blueprint? ') 
                                if take.lower() == ('yes') or take.lower() == ('y'):
                                        print('You roll up the mysterious BLUEPRINT and stash it in your haversack.')
                                        player.inventory.update({'BLUEPRINT': "A mysterious blueprint you found on the ground."})
                                if take.lower() == ('no') or take.lower() == ('n'):
                                        print('You decide to travel light.')
                                while take.lower() not in ['yes', 'y', 'no', 'n']:
                                        print("Not a valid command.")
                                        take = input('Take the blueprint? ') 
                                        if take.lower() == ('yes') or take.lower() == ('y'):
                                                print('You roll up the mysterious BLUEPRINT and stash it in your haversack.')
                                                player.inventory.update({'BLUEPRINT': "A mysterious blueprint you found on the ground."})
                                        if take.lower() == ('no') or take.lower() == ('n'):
                                                print('You decide to travel light.')

                elif response.lower() == ('manager'):
                        if 'CELLPHONE' not in player.inventory:
                                print("You try calling your manager... but you don't have a phone.")
                        if 'CELLPHONE' in player.inventory:
                                print("You dial your manager's phone number.")
                                time.sleep(2)
                                print('ring...')
                                time.sleep(2)
                                print('ring...')
                                time.sleep(2)
                                manager_dlg = "Meow? Oh, hi " +str(player.name) +"! How's the test going?... oh? Well, I suppose I can help you a little bit. I heard..."
                                for character in manager_dlg:
                                                sys.stdout.write(character)
                                                sys.stdout.flush()
                                                time.sleep(0.03)
                                manager_dlg = list_random(MANAGER_SAYS)
                                for character in manager_dlg:
                                                sys.stdout.write(character)
                                                sys.stdout.flush()
                                                time.sleep(0.03)
                elif response.lower() == ('conbini'):
                        print('You recall that Advenuring Solutions Inc. owns a chain of convenience stores called "Conbini".')
                        print("They've been popping up everywhere--There might even be one down here!")
                        search_conbini = input('Search for a Conbini?')
                        if search_conbini.lower() == ('yes') or search_conbini.lower()== ('y'):
                                if 'CELLPHONE' not in player.inventory:
                                        print("Fortunately, it doesn't take long to find. Simply visualizing it seems to make it appear!")
                                        time.sleep(2)
                                        print('The convenience store is a blessed oasis of flourescent light amidst the darkness of the labyrinth.')
                                        time.sleep(2)
                                        print('As you walk in the door chimes and a friendly looking calico greets you.')
                                        time.sleep(2)
                                        print('"Welcome to our store, nyaaa~", says the cat.')
                                        time.sleep(2)
                                        print("'We're running a special promotion: new customers get a free cellphone!'" )
                                        time.sleep(2)
                                        print('The calico shoves a new VentureTech 5X cellphone into your hands.')
                                        player.inventory.update({'CELLPHONE': "The latest model of the VentureTech phone!"})
                                        print('"And it comes preloaded with Serpent Sojourn III!", the calico adds. Sweet!')
                                elif 'CELLPHONE' in player.inventory:
                                        print("You see the old hermit browsing the magazine wrack.")
                                        time.sleep(2)
                                        print('He spots you, gives a short nod, and says, "Sup."')
                                        time.sleep(2)
                                        print('You respond in kind.')
                                        time.sleep(2)
                                        print('You then casually browse the VentureTech games. You cannnot afford any of them.')
                        if search_conbini.lower() == ('no') or search_conbini.lower()==('n'):
                                print('You decide to not search for a Conbini.')
                        while search_conbini.lower() not in ['yes','y','no','n']:
                                print('Not a valid command.')
                                search_conbini = input('Search for a Conbini?')
                                if search_conbini.lower() == ('yes') or search_conbini.lower()== ('y'):
                                        if 'CELLPHONE' not in player.inventory:
                                                print("Fortunately, it doesn't take long to find. Simply visualizing it seems to make it appear!")
                                                time.sleep(2)
                                                print('The convenience store is a blessed oasis of flourescent light amidst the darkness of the labyrinth.')
                                                time.sleep(2)
                                                print('As you walk in the door chimes and a friendly looking calico greets you.')
                                                time.sleep(2)
                                                print('"Welcome to our store, nyaaa~", says the cat.')
                                                time.sleep(2)
                                                print("'We're running a special promotion: new customers get a free cellphone!'" )
                                                time.sleep(2)
                                                print('The calico shoves a new VentureTech 5X cellphone into your hands.')
                                                player.inventory.update({'CELLPHONE': "The latest model of the VentureTech phone!"})
                                                print('"And it comes preloaded with Serpent Sojourn III!", the calico adds. Sweet!')
                                        elif 'CELLPHONE' in player.inventory:
                                                print("You see the old hermit browsing the magazine wrack.")
                                                time.sleep(2)
                                                print('He spots you, gives a short nod, and says, "Sup."')
                                                time.sleep(2)
                                                print('You respond in kind.')
                                                time.sleep(2)
                                                print('You then casually browse the VentureTech games. You cannnot afford any of them.')
                                if search_conbini.lower() == ('no') or search_conbini.lower()==('n'):
                                        print('You decide to not search for a Conbini.')

                elif response.lower() == ('inventory'):
                        print('Your haversack currently contains... ' +str(player.inventory) +".")

                elif response.lower() == ('help'):
                        print('A strange voice from above speaks to you.')
                        time.sleep(2)
                        print('Enter "start" to start the game.\n Enter "skip" to start the game without the intro.\nYou will often be prompted to type "yes" or "no" or a keyword.\nA keyword will be printed in all CAPS.')
                        print('You will start with 100 HP and 100 MP.\nIf your HP reaches 0 you will lose the game. You can use your MP to cast magic to avoid this.\nDo you understand?')
                        understood = input('\n> ')
                        if understood.lower() ==  ('yes') or understood.lower() == ('y'):
                                print('Very good. Keep at it! I have faith in you!')
                        if understood.lower() == ('no') or understood.lower() == ('n'):
                                print('Really? You seem to have a grasp of the basics.')
                                time.sleep(2)
                                
                        while understood.lower() not in ['yes', 'y', 'no', 'n']:
                                print('Just type "yes", "no", "y", or "n". Do you understand?')
                                understood = input('\n> ')
                                if understood.lower() ==  ('yes') or understood.lower() == ('y'):
                                    print('Very good. Keep at it! I have faith in you!')

                                if understood.lower() == ('no') or understood.lower() == ('n'):
                                        print('Really? You seem to have a grasp of the basics.')
                                        time.sleep(2)
                                
                elif response.lower() == ('crit'):

                        if 'BLUEPRINT' in player.inventory:
                                print('You have found a hangar bay housing a huge bipedal mech!')
                                time.sleep(2)
                                print('You quickly recognize the design as the same as that on the blueprints.')
                                time.sleep(2)
                                print('With your knowledge from the blueprints, you hop into the cockpit and initiate a systems diagnostic.')
                                time.sleep(2)
                                print('Congratulations! The Omega Weapon Mk. I is fully armed and operational!')
                                player.inventory.update({'OMEGA WEAPON': 'A bipedal death machine.'})
                                print('You can now explore the labyrinth from the safety and comfort of the Omega Weapon!')

                        elif 'BLUEPRINT' not in player.inventory:
                                print('You have found a hangar bay housing a huge bipedal mech!')
                                time.sleep(2)
                                print('Unfortunately, you do not have the technical know-how to pilot it...')
                                time.sleep(2)
                                print('You return to where you came from, but you make a special note of this place.')

                        elif 'OMEGA WEAPON' in player.inventory:
                        		print('You already have the Omega Weapon. There is nothing else here.')





                else:
                        print('You gaze into the abyss of the labyrinth, and the abyss gazes back...')
                        print('Please enter a valid command.')
#### Rolls the Dice for random encounters ####

def roll_the_dice():
                os.system('cls')
                player.times_explored =  player.times_explored + 1
                die_roll = random.randint(1,14)
                if die_roll in DONUTS:
                        print("You got a donut! Yum!")
                        eat_donut()
                        print("Your HP is " + str(player.health) +".")
                        print("Your MP is " + str(player.mp) +".")
                elif die_roll in COFFEE:
                        print("You got a cup of coffee! Slurp! Ah~")
                        drink_coffee()
                        print("Your HP is " + str(player.health) +".")
                        print("Your MP is " + str(player.mp) +".")
                elif die_roll in BANDERSNATCH:
                        battle = True
                        while battle == True:
                                battack = 'The bandersnatch lunges at you! Do you FIGHT back or cast FIRE?\n'
                                for character in battack:
                                        sys.stdout.write(character)
                                        sys.stdout.flush()
                                        time.sleep(0.03)
                                action = input('> ')
                                if action.lower() == 'fight':
                                        print("You fight off the bandersnatch but take some damage in the process!\n")
                                        bandersnatch()
                                        print("Your HP is " + str(player.health) +".")
                                        print("Your MP is " + str(player.mp) +".")
                                        battle = False
                                if action.lower() == 'fire':
                                        fire()
                                        time.sleep(1)
                                        print("You drove off the bandersnatch with fire!\n")
                                        battle = False
                                else:
                                        print("You can't do that now.")
                elif die_roll in FAIRY:
                        print("You found a lost fairy!")
                        fairy()
                        print("Your HP is " + str(player.health) +".")
                        print("Your MP is " + str(player.mp) +".")
                elif die_roll in EXITLABYRINTH:
                        print("You found the exit to the labyrinth!")
                        print("Your HP is " + str(player.health) +".")
                        print("Your MP is " + str(player.mp) +".")
                        print("You explored the labyrinth " + str(player.times_explored) + " times!")
                        print()
                        print('You can leave this place or continue exploring.')
                        leave = input('Leave?')
                        if leave.lower() == ('yes') or leave.lower() == ('y'):
                                player.game_on = False
                        if leave.lower() == ('no') or leave.lower() == ('n'):
                                explore()
                        
                elif die_roll in TRAP:
                        print("You walked into a trap! Ouch!")
                        trap()
                        print("Your HP is " + str(player.health) +".")
                        print("Your MP is " + str(player.mp) +".")

                elif die_roll in HERMIT:
                        hermit = 'You find a mysterious old hermit. He says to you...\n'
                        for character in hermit:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.03)
                        time.sleep(2)
                        say = list_random(HERMIT_SAYS)
                        for character in say:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.05)
        
####Sets up the game, asks for player name, etc.
def intro():
        os.system('cls')

        intro = """Welcome to Coffee and Donuts: a Special Employee Training Simulator by Adventuring Solutions Inc. 
If you are reading this it is because your supervisor, MANAGER Cat, with the approval of CEO Top Cat, has recommeneded you for
our special employee training program. The objective of the simulation is simple. You must escape the company labyrinth.
Your objective, however, is to put the simulator through its paces and determine whether or not it is ready for market-release.
Remember, our products are intended for a wide range of adventurers and dungeoneers, and must be looked at CRITically from
their PERSPECTIVE."""
        intro_clean = textwrap.fill(intro, width = 60)
        print(intro_clean)
        print()
        print("\n***SIMULATION COMMENCING***")
        print()
        print("\nPress 'enter' to continue")
        input()
        

def setup_game():
        os.system('cls')

        
        question1 = "Hello, what is your name?\n"
        for character in question1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.03)
        player_name = input("> ")
        player.name = player_name

        question2 = "Are you ready to explore the labyrinth, " +player.name+ "?\n"
        for character in question2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.03)
        answer1 = input("> ")
        if answer1.lower() == ('yes') or answer1.lower() == ('y'):
                roll_the_dice()
        if answer1.lower() == ('no')or answer1.lower() == ('n'):
                title_screen()
        while answer1.lower() not in ['yes', 'y', 'no', 'n']:
                print('Please enter a valid command.')
                answer1 = input("> ")
                if answer1.lower() == ('yes') or answer1.lower() == ('y'):
                        roll_the_dice()
                if answer1.lower() == ('no')or answer1.lower() == ('n'):
                        title_screen()





#####THE MAIN PROGRAM BEGINS HERE#####
player = player()
#score = (player.health + player.mp)*player.times_explored ##For some reason this keeps returning 0

while True:

        title_screen()
        explore()
        
        print('Your score is ' + str((player.health + player.mp + player.keywords_used)*player.times_explored) + '.')
        print('You used keywords ' +str(player.keywords_used)+ ' times and explored the labyrinth '+ str(player.times_explored)+ ' times.')
        answer = input('Play again? (y/n): ')
        if answer == 'n' or  answer == 'no':
            exit()
        if answer == 'y' or answer == 'yes':
                player.health = 100
                player.mp = 100
                player.times_explored = 0
                player.keywords_used = 0
                player.inventory = {}
                player.game_on = True
                continue
        while answer not in ['y','yes','n','no']:
            print ('Please enter a valid command.')
            answer = input('Play again? (y/n): ')
            if answer == 'n' or answer == 'no':
                exit()
            if answer == 'y' or answer == 'yes':
                        player.health = 100
                        player.mp = 100
                        player.times_explored = 0
                        player.keywords_used = 0
                        player.game_on = True
                        continue
                

