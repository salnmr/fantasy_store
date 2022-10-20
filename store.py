# fantasy store sim
import sys
from colorama import Fore, Back, Style

shop = {}

player = {"name": "Player"}

state = {"intro_done": False}


def intro():
    print("Shop Keeper: Welcome to my shop! What is your name traveler? \n")
    character_creation()


# Asks name and then checks to make sure they want that name. Passes through check_player_input func
def character_creation():
    while True:
        possible_player_name = check_player_input(player["name"])

        print(f"Hmmmm... {possible_player_name.capitalize()}. Did I get that right? (Y)es or (N)o\n")
        confirm_player_name = check_player_input(player["name"])

        if confirm_player_name == "y" or confirm_player_name == "yes":
            player["name"] = possible_player_name.capitalize()
            break
        elif confirm_player_name == "n" or confirm_player_name == "no":
            print("Hmmm.. ok. Lets try again What is your name? \n")
            continue
        else:
            print("Hmmmm thats not (Y)es or (N)o.  Lets start over, shall we. What is your name? \n")
            continue


# Merely checks to see if player inpout is a valid number or word. No blanks, special chars, " ".
# Does not check shop or inventory
def check_player_input(name):
    player_input = input(f"{name}: ").strip().lower()
    if player_input == "quit" or player_input == "q":
        "\nGood bye!"
        sys.exit()

    try:
        if bool(player_input):
            if player_input.isalpha() or player_input.isdigit():
                if player_input.isalpha():
                    return player_input.lower()
                else:
                    return player_input
            else:
                raise AttributeError
        else:
            raise AttributeError
    except AttributeError:
        print("Look buddy... I need either a word or letter... Not blank. Nor any special characters. IT'S NOT HARD! \n")


# main loop
while True:
    if not state["intro_done"]:
        intro()
        state["intro_done"] = True
    check_player_input(player["name"])




