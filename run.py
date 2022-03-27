"""
high level support for doing this and that.
"""
import random
# import time
# import sys


# import random


# def boss_abilities():


def boss_encounter():
    boss_hit = random.randint(0, 200)
    print(boss_hit)


def welcome():
    """
        We introduce the user to the game and let the user choose role.
        We return to this function every time we want the game to reset.
    """
    print("CHAMPION! I have been waiting for you!")
    print("We need help slaying this beast! What role would you like to play?")


def tank_info():
    """
    This function implements all your abilities as a tank player
    """
    print("Champion! Prepare yourself! And don't forget to use your abilities")
    print("Press 1 to strike the boss")
    print("Press 2 to use a defensive from heavy hitting abilities")
    print("Press 3 to protect the entire group")
    print("Press 4 to hide from the boss's main ability")


def healer_info():
    """
    This function implements all your abilities as a healer player
    """
    print("Champion! Prepare yourself! And don't forget to use your abilities")
    print("Press 1 to strike the boss")
    print("Press 2 to heal the tank")
    print("Press 3 to protect the entire group for a few seconds")
    print("Press 4 to hide from the boss's main ability")


def dps_info():
    """
    This function implements all your abilities as a dps player
    """
    print("Champion! Prepare yourself! And don't forget to use your abilities")
    print("Press 1 to strike the boss")
    print("Press 2 to use a defensive from heavy hitting abilities")
    print("Press 3 to protect the entire group")
    print("Press 4 to hide from the boss's main ability")


def main():
    """
    This is the main function
    """
    # player_health = 1000
    # boss_health = 1000
    welcome()
    role_choice = input("Type 'tank', 'healer' or 'dps' to choose.")
    if role_choice == "tank":
        tank_info()
    elif role_choice == "healer":
        healer_info()
    elif role_choice == "dps":
        dps_info()
    else:
        print("Please input a valid role")
    print(f"Fantastic choice, a {role_choice} is just what we need!")
    boss_encounter()


main()
