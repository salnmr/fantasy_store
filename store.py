# fantasy store sim
import random
import sys
from colorama import Fore, Style

shopkeeper = {"gold": 1000}
shop_inventory = {"rusty sword": {"quantity": 1, "price": 60},
                  "arrow": {"quantity": 10, "price": 5},
                  "flimsy bow": {"quantity": 1, "price": 45}}

player = {"name": "Player", "gold": 100, "adventure_lose": 0}
player_inventory = {"lint": {"quantity": 10, "price": 1}}

state = {"intro_done": False}

loot_table = {"bush": {'Bronze bar': {"quantity": 1, "price": 25},
                       'Bread': {"quantity": 1, "price": 10},
                       'lint': {"quantity": 10, "price": 1},
                       'broken tool': {"quantity": 5, "price": 30}},
              "old_house": {'Pile of Silver bars': {"quantity": 3, "price": 50},
                            'Wand of Kal\' Dread': {"quantity": 1, "price": 100},
                            'Scroll of Protection': {"quantity": 1, "price": 150}},
              "smoking_cave": {'Pile of Gold bars': {"quantity": 10, "price": 100},
                               'Orb of Driscul': {"quantity": 1, "price": 300},
                               'Ye Olden\' Sword of Super Utter Calamity': {"quantity": 1, "price": 750}}}


def intro():
    print("Shop Keeper: Welcome to my shop! What is your name traveler?")
    character_creation()
    print(f"""Shop Keeper: WELL! {player['name']}, nice to meet you!""")
    print("- To go home type '(H)ome')")
    print("- To quit type '(Q)uit')")


# Asks name and then checks to make sure they want that name.
# Passes through check_player_input func
def character_creation():
    while True:
        possible_player_name = check_player_input(player["name"])
        try:
            print(f"Hmmmm... {possible_player_name.capitalize()}... Did I get that right? "
                  f"(Y)es or (N)o")
            confirm_player_name = check_player_input(player["name"])

            # loop to ensure the player wants their name
            if confirm_player_name == "y" or confirm_player_name == "yes":
                player["name"] = possible_player_name.capitalize()
                break
            elif confirm_player_name == "n" or confirm_player_name == "no":
                print("Hmmm.. ok. Lets try again What is your name?")
                continue
            else:
                print("Lets start over, shall we. What is your name?")
                continue
        # catches trying to capitalize "" since it is none. This happens if
        # the user enters nothing right from the start
        except AttributeError:
            pass


# Checks to see if the user wants to quit or go home (leave the wilderness)
# Checks to see if player input is a valid number or a word. No blanks, special chars, " ".
def check_player_input(name):
    player_input = input(f"{name}: ").strip().lower()
    if player_input == "quit" or player_input == "q":
        "Good bye!"
        sys.exit()
    elif player_input == "home" or player_input == "h":
        interact_with_shop_keeper()

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
        # change the color of the warning
        print(Fore.LIGHTBLUE_EX + "Shop Keeper: Look buddy... I need either a word or "
                                  "letters... Nothing blank! Not ~,*, or %! Nothing! IT'S NOT HARD!")
        # stop color change
        print(Style.RESET_ALL, end="")


def interact_with_shop_keeper():
    print(
        """Shop Keeper: What can I do for you?
    1). (B)uy
    2). (S)ell
    3). (T)rade
    4). (P)rint (P)layer Inventory
    5). (P)rint (S)hop Inventory
    6). (A)dventure for treasure!
    7). (R)est""")
    player_choice = check_player_input(player["name"])

    if player_choice == "1" or player_choice == "b" or player_choice == "buy":
        buy()
    elif player_choice == "2" or player_choice == "s" or player_choice == "sell":
        sell()
    elif player_choice == "3" or player_choice == "t" or player_choice == "trade":
        trade()
    elif player_choice == "4" or player_choice == "pp" or player_choice == "print player inventory":
        print_inventory("player")
    elif player_choice == "5" or player_choice == "ps" or player_choice == "print shop inventory":
        print_inventory("shop")
    elif player_choice == "6" or player_choice == "a" or player_choice == "adventure for treasure":
        adventure_for_treasure()
    elif player_choice == "7" or player_choice == "r" or player_choice == "rest":
        rest()
        interact_with_shop_keeper()
    else:
        # if the user enters anything else the shop keeper will restart
        interact_with_shop_keeper()


def buy():
    pass


def sell():
    pass


def trade():
    # trade with shop.
    #     Trade works as such. Trade 10 arrows at 10gp each for x1 100gp sword. easy.
    #     Trade 8 arrow at 10gp each for x1 100gp sword. Wont work.
    #     however, if the shop keeper says he likes you (sell him 5 items)
    #     he will allow for a 20gp differnce
    pass


def rest():
    # have it cost money
    player["adventure_lose"] = 0


def adventure_for_treasure():
    # check to make sure player can keep adventuring. If they cant send them back to shop
    if player["adventure_lose"] >= 4:
        print("You feel tired. Go rest at the shop")
        interact_with_shop_keeper()

    print(
        """Do you walk into the...
    1). (B)ushes
    2). (O)ld House
    3). (S)moking Cave (Why, is it smoking?)""")
    player_choice = check_player_input(player["name"])
    wild_random_roll = random.randint(1, 105)
    player_random_roll = random.randint(1, 105)

    if player_choice == "1" or player_choice == "b" or player_choice == "bushes":
        print("A WILD! Hob-Goblin appears")
        wild_random_roll += 5
        if player_random_roll > wild_random_roll:
            print("you won!")
            player_loot_corspe("bush")
            check_adventure_again()
        else:
            player["adventure_lose"] += 1
            print("you lost")
            check_adventure_again()

    elif player_choice == "2" or player_choice == "o" or player_choice == "old house":
        print("A WILD! Wraith appears!")
        wild_random_roll += 15
        if player_random_roll > wild_random_roll:
            print("you won!")
            player_loot_corspe("old_house")
            check_adventure_again()
        else:
            player["adventure_lose"] += 3
            print("you lost")
            check_adventure_again()

    elif player_choice == "3" or player_choice == "s" or player_choice == "smoking cave":
        print("Ahhhh shit... it's a Dragon!")
        wild_random_roll += 5
        if player_random_roll > wild_random_roll:
            print("you won!")
            player_loot_corspe("smoking_cave")
            check_adventure_again()
        else:
            print("You got your ass kicked and hobbled back to town with none of your items...")
            player["adventure_lose"] += 5
            # ADD remove  all the items

            interact_with_shop_keeper()


def print_inventory(which_inventory):
    if which_inventory == "player":
        inventory = player_inventory
        print("** Player Inventory ** ")
    # shop inventory
    else:
        inventory = shop_inventory
        print("-- Store Inventory --")

    for key, value in inventory.items():
        print(f"x{value['quantity']} - {key} - {value['price']}gp")


def player_loot_corspe(mob):
    # choose random item in dic
    # for key, value in loot_table[mob].items():
    #     print(key, "key")
    #     print(value, "val")
    #     print(key.get())
    print(random.choice(loot_table[mob]))

    # if quainity > 1. randomise amount
    # add to player invetory.

    # if no items in loot table. say 'you killed everything'
    # try:
    # del loot_table["bush"]
    # print("loot table", loot_table)
    # print("mob", mob)
    # if len(mob) > 1:
    #     print("stuff here")

    # except Exception as e:
    #     print(e, 'error')
    # print("you killed everything")
    # interact_with_shop_keeper()


def check_adventure_again():
    # check to make sure player can keep adventuring. If they cant send them back to shop prevents
    #  user being asked to cont after adventure_lose is brought over limit and this func is called
    if player["adventure_lose"] >= 4:
        print("You feel tired. Go rest at the shop")
        interact_with_shop_keeper()

    print("Do you want to adventure again? (Y)es or (N)o?")
    player_choice = check_player_input(player["name"])

    while player["adventure_lose"] <= 4:
        if player_choice == "y" or player_choice == "yes":
            adventure_for_treasure()
        elif player_choice == "n" or player_choice == "no":
            print("Shop Keeper: That's enough adventuring for today! Rest for a bit.")
            interact_with_shop_keeper()
        # this accounts for " " in the check_adventure_again
        else:
            print("Lets try again.... Do you want to adventure again? (Y)es or (N)o?")
            player_choice = check_player_input(player["name"])


# main loop
while True:
    if not state["intro_done"]:
        intro()
        state["intro_done"] = True
    interact_with_shop_keeper()

# create loop corspe func
# lose all items if die on smoking cave
# have rest cost gold
