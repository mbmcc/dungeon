import os
import random

welcome = """
        Welcome to the dungeon!
        You'll need to solve puzzles, sneak, make friends and defeat enemies to escape
        """

def clear_screen():
     os.system('clear')

def print_screen(*args):
    os.system('clear')
    for words in args:
        print(words)


#clear_screen()
#print(welcome)

print_screen(welcome)

## encounter
choose_again = 'true'
choice_text= """
(a)ttack (w)alk (r)etreat (s)neak (t)alk (u)se item
"""
valid_actions = [
"a", "attack", "w", "walk", "r", "retreat", "s", "sneak", "t", "talk", "u", "use item"  
]
 
while choose_again:
    valid_choice = False
    player_action = input(choice_text)
    print_screen("player_action is ", player_action)
    for item in valid_actions:
        if player_action == item: 
            print("matched item is ", item)
            valid_choice = True
            choose_again = False
            break

    if valid_choice == False:
        print("please choose a valid option")


##------
#if player_action == "f":
#    print("you chose to fight")
#    choose = "false"
#
#elif player_action == "r":
#    print("you chose to run")
#
#elif player_action == "d":
#    print("you chose to do")
#
#elif player_action == "u":
#    print("you chose to use")
#
print("game over")

