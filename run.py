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
    response = input("Do you remember how to play? yes/no\n")
    if response == "no":
        print("Press 1 to strike the boss")
        print("Press 2 to use a defensive from heavy hitting abilities")
    elif response == "yes":
        print("Excellent! Let's start the fight")
    else:
        print("Please respond yes or no")
        tank_info()


def healer_info():
    """
    This function implements all your abilities as a tank player
    """
    response = input("Do you remember how to heal? yes/no\n")
    if response == "no":
        print("Press 1 to strike the boss")
        print("Press 2 to heal the tank when they get low on health")
    elif response == "yes":
        print("Excellent! Let's start the fight")
    else:
        print("Please respond yes or no")
        healer_info()


def boss_hit():
    """
    The damage dealt by the boss, a random number between 20 and 100
    """
    hit = random.randint(20, 100)
    print(f"The boss hit for {hit} damage!")
    return hit


def player_hit():
    """
    Damage dealt by the player to the boss, random amount between 0 and 80
    """
    hit = random.randint(0, 80)
    print(f"You hit for {hit}")
    return hit


def player_heal():
    """
    Player healing ability
    """
    heal = random.randint(100, 150)
    print(f"You heal for {heal}")
    return heal


def main():
    """
    This is the main function
    """
    player_health = 300
    boss_health = 1000
    role_choice = input("Type 'tank', 'healer' or 'dps' to choose.\n")
    if role_choice == "tank":
        tank_info()
        print("Champion! Prepare yourself! Don't forget to use your abilities")
        while boss_health and player_health > 0:
            print(f"HP: {player_health}")
            print(f"BOSS HP: {boss_health}")
            action = int(input("Attack or heal\n"))
            if action == 1:
                boss_health = boss_health - player_hit()
            elif action == 2:
                player_health = player_health + player_heal()
            else:
                print("You messed up, the boss strikes you twice. Ouch!")
                player_health = player_health - boss_hit()
            player_health = player_health - boss_hit()

        if boss_health == 0:
            print("Congratulations! You defeated the boss!")
        else:
            input("The boss is laughing, you should try the boss again?\n")

    elif role_choice == "healer":
        healer_info()
        print("Champion! Prepare yourself! Don't forget to use your abilities")
        while boss_health and player_health > 0:
            print(f"Tank HP: {player_health}")
            print(f"BOSS HP: {boss_health}")
            action = int(input("Attack or heal the tank\n"))
            if action == 1:
                boss_health = boss_health - player_hit()
            elif action == 2:
                player_health = player_health + player_heal()
            else:
                print("You messed up, the boss striked the tank twice. Ouch!")
                player_health = player_health - boss_hit()
            player_health = player_health - boss_hit()

        if boss_health == 0:
            print("Congratulations! You defeated the boss!")
        else:
            input("The boss is laughing, you should try the boss again?\n")

    else:
        print("Please choose a valid role")
        main()


welcome()
main()
