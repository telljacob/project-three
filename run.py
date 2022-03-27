"""
high level support for doing this and that.
"""
import random


def welcome():
    """
        We introduce the user to the game and let the user choose role.
        We return to this function every time we want the game to reset.
    """
    print("CHAMPION! I have been waiting for you!")
    print("We need help slaying this beast! What role would you like to play?")
    print()


def tank_info():
    """
    This function implements all your abilities as a tank player
    """
    print()
    response = input("Do you remember how to play tank? yes/no\n")
    if response == "no":
        print()
        print("The tank fights the beast, the healer helps you stay alive.")
        print("Press 1 to strike the boss.")
        print("Press 2 to use a defensive from heavy hitting abilities.")
    elif response == "yes":
        print()
        print("Excellent! Let's start the fight")
    else:
        print("Please respond yes or no")
        tank_info()


def healer_info():
    """
    This function implements all your abilities as a tank player
    """
    print()
    response = input("Do you remember how to heal? yes/no\n")
    if response == "no":
        print()
        print("As the healer it is your job to keep the tank alive.")
        print("Press 1 to strike the boss when the tank has high health.")
        print("Press 2 to heal the tank when they get low on health.")
    elif response == "yes":
        print()
        print("Excellent! Let's start the fight")
    else:
        print("Please respond yes or no")
        healer_info()


def boss_hit():
    """
    The damage dealt by the boss, a random number between 20 and 100
    """
    hit = random.randint(50, 90)
    print(f"The boss hit for {hit} damage!")
    return hit


def player_hit():
    """
    Damage dealt by the player to the boss, random amount between 0 and 80
    """
    hit = random.randint(85, 120)
    print(f"You hit for {hit}")
    return hit


def player_heal():
    """
    Player healing ability
    """
    heal = random.randint(130, 200)
    print(f"You heal for {heal}")
    return heal


def tank():
    """
    Function runs if the player decides to play as a tank
    """
    player_health = 300
    boss_health = 1000
    tank_info()
    while boss_health and player_health > 0:
        print()
        print(f"HP: {player_health}")
        print(f"BOSS HP: {boss_health}")
        action = int(input("Attack or heal\n"))
        if action == 1:
            boss_health = boss_health - player_hit()
        elif action == 2:
            player_health = player_health + player_heal()
        else:
            print()
            print("You messed up, the boss strikes you twice. Ouch!")
            player_health = player_health - boss_hit()
        player_health = player_health - boss_hit()

    if boss_health == 0:
        print("Congratulations! You defeated the boss!")
        main()
    else:
        print("The boss is laughing, Try again!\n")
        main()


def healer():
    """
    Function runs if the user decides to play as a healer
    """
    player_health = 300
    boss_health = 1000
    healer_info()
    while boss_health and player_health > 0:
        print()
        print(f"Tank HP: {player_health}")
        print(f"BOSS HP: {boss_health}")
        action = int(input("Attack or heal the tank\n"))
        if action == 1:
            boss_health = boss_health - player_hit()
        elif action == 2:
            player_health = player_health + player_heal()
        else:
            print()
            print("You messed up, the boss striked the tank twice. Ouch!")
            player_health = player_health - boss_hit()
        player_health = player_health - boss_hit()

    if boss_health == 0:
        print("Congratulations! You defeated the boss!")
    else:
        input("The boss is laughing, you should try the boss again?\n")


def main():
    """
    This is the main function
    """
    while True:
        try:
            role_choice = input("Type 'tank' or 'healer' to choose.\n")

        except ValueError:
            print("That is not correct, please select one of the above roles")
            continue
        else:
            break
    if role_choice == "tank":
        tank()
    elif role_choice == "healer":
        healer()


welcome()
main()
