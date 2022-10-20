# fantasy store sim
import sys
from colorama import Fore, Back, Style

shop_inventory = {"sword": {"quantity": 1, "price": 60}, "arrow": {"quantity": 10, "price": 5}}

player = {"name": "Player", "gold": 100}

player_inventory = {}

state = {"intro_done": False}


def intro():
    print("Shop Keeper: Welcome to my shop! What is your name traveler? \n")
    character_creation()
    print(f"Shop Keeper: WELL! {player['name']}, nice to meet you!")


# Asks name and then checks to make sure they want that name. Passes through check_player_input func
def character_creation():
    while True:
        possible_player_name = check_player_input(player["name"])
        try:
            print(f"Hmmmm... {possible_player_name.capitalize()}... Did I get that right? (Y)es or (N)o\n")
            confirm_player_name = check_player_input(player["name"])

            if confirm_player_name == "y" or confirm_player_name == "yes":
                player["name"] = possible_player_name.capitalize()
                break
            elif confirm_player_name == "n" or confirm_player_name == "no":
                print("Hmmm.. ok. Lets try again What is your name? \n")
                continue
            else:
                print("Lets start over, shall we. What is your name? \n")
                continue
        except AttributeError:
            pass

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
        print(Fore.MAGENTA + "Look buddy... I need either a word or letter... Not blank. Nor any special characters. IT'S NOT HARD!")
        print(Style.RESET_ALL)


def interact_with_shop_keeper():
    print("""
    Shop Keeper: What can I do for you? (*Also, to go home type 'home')
    1). Buy
    2). Sell
    3). Trade
    
    4). Print your Inventory
    5). Print Shop Inventory
    """)
    player_choice = check_player_input(player["name"])
    print(player_choice)

# print shop inv
# print player inv
# buy from show
# sell to shop
# trade with shop.
#     Trade works as such. Trade 10 arrows at 10gp each for x1 100gp sword. easy.
#     Trade 8 arrow at 10gp each for x1 100gp sword. Wont work.
#     however, if the shop keeper says he likes you (sell him 5 items) he will allow for a 20gp differnce


def write_shop_inv():
    print("mah shop")

# main loop
while True:
    if not state["intro_done"]:
        intro()
        state["intro_done"] = True
    interact_with_shop_keeper()






