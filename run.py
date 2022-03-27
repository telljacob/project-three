"""
high level support for doing this and that.
"""
import random
# import time
# import sys


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
    response = input("Do you remember how to tank this boss? yes/no")
    if response == "no":
        print("Press 1 to strike the boss")
        print("Press 2 to use a defensive from heavy hitting abilities")
        print("Press 3 to hide from the boss's main ability")
    elif response == "yes":
        print("Excellent! Let's start the fight")
    else:
        print("Please respond yes or no")
        tank_info()


def healer_info():
    """
    This function implements all your abilities as a healer player
    """
    response = input("Do you remember how to heal this boss? yes/no")
    if response == "no":
        print("Press 1 to strike the boss")
        print("Press 2 to heal the tank")
        print("Press 3 to hide from the boss's main ability")
    elif response == "yes":
        print("Excellent! Let's start the fight")
    else:
        print("Please respond with yes or no")
        healer_info()


def boss_hit():
    hit = random.randint(0, 100)
    print(f"The boss hit for {hit} damage!")


def player_hit():
    """
    Damage dealt by the player to the boss.
    """
    hit = random.randint(0, 80)
    return print(f"You hit for {hit}")


def player_heal():
    """
    Player healing ability
    """
    heal = random.randint(100, 150)
    PLAYER_HEALTH += heal
    return print(f"You heal for {heal}")


def player_choice(num):
    """
    Player chooses what action to take
    """
    if num == 1:
        player_hit()
    elif num == 2:
        player_heal()
    else:
        print("You pressed something wrong! Oh no!")


def main():
    """
    This is the main function
    """
    player_health = 300
    boss_health = 1000
    role_choice = input("Type 'tank', 'healer' or 'dps' to choose.\n")
    if role_choice == "tank":
        tank_info()
    elif role_choice == "healer":
        healer_info()
    else:
        print("Please choose a valid role")
        main()

    print("Champion! Prepare yourself! And don't forget to use your abilities")

    while boss_health and player_health > 0:
        boss_hit()
        print(f"HP: {player_health}")
        print(f"BOSS HP: {boss_health}")
        action = int(input("Attack or heal"))
        player_choice(action)

    if boss_health == 0:
        input("Congratulations! You defeated the boss!")
    else:
        input("The boss is laughing, would you like to try the boss again?")


welcome()
main()
