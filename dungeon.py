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

def get_choice():
    choose_again = 'true'
    while choose_again:
        choice_text= """
 What do you want to do?:

 (a)ttack (m)ove (l)ook (s)neak (t)alk (u)se item
        """
        valid_actions = [
        "a", "attack", "m", "move", "l", "look", "s", "sneak", "t", "talk", "u", "use item"  
        ]
        valid_choice = False
        player_action = input(choice_text)
        
        for option in valid_actions:
            if player_action == option: 
                return option
                valid_choice = True
                choose_again = False
                break

        if valid_choice == False:
            print_screen("please choose a valid option")


if __name__ == "__main__":
    main()


def main():
    print_screen(welcome)
    input()
    print_screen("""
 You see a shadowy figure in the distance. 
            """)
    choice = get_choice()
    print_screen(" You chose ", choice)
    input()

    print("game over")


