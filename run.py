"""
high level support for doing this and that.
"""
import random


def welcome():
    """
        We introduce the user to the game.
        This will only show the very first time the program runs.
    """
    print("CHAMPION! I have been waiting for you!")
    print("We need your help killing this beast.")
    print()


def tank_info():
    """
    This function introduces the user to the tank role and
    asks the user if they are familiar with the role
    or want a more in depth explanation.
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
    This function introduces the user to the healer role and
    asks the user if they are familiar with the role
    or want a more in depth explanation.
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
    The damage dealt by the boss, a random number between 50 and 90 through
    random.randint
    """
    hit = random.randint(50, 90)
    print(f"The boss hit for {hit} damage!")
    return hit


def player_hit():
    """
    Damage dealt by the player to the boss, a random number between 85 and 120
    through random.randint
    """
    hit = random.randint(85, 120)
    print(f"You hit for {hit} damage!")
    return hit


def player_heal():
    """
    Player heal, a random number between 130 and 200 through random.randint
    """
    heal = random.randint(130, 200)
    print(f"You heal for {heal}!")
    return heal


def tank():
    """
    Function runs if the player decides to play as a tank.
    All the combat with a tank role will be done in this function.
    """
    player_health = 300
    boss_health = 1000
    tank_info()
    while boss_health > 0 and player_health > 0:
        print()
        print(f"Your HP: {player_health}")
        print(f"BOSS HP: {boss_health}")
        action = int(input("Attack(1) or heal(2)\n"))
        if action == 1:
            boss_health = boss_health - player_hit()
        elif action == 2:
            player_health = player_health + player_heal()
        else:
            print()
            print("You messed up, the boss strikes you twice. Ouch!")
            player_health = player_health - boss_hit()
        player_health = player_health - boss_hit()

    if boss_health <= 0:
        print("Congratulations! You defeated the boss!")
        main()
    else:
        answer = input("You died, do you want to try again? yes/no\n")
        if answer == "yes":
            main()
        else:
            print("Thank you for trying out my game :)")


def healer():
    """
    Function runs if the player decides to play as a healer.
    All the combat with a healer role will be done in this function.
    """
    player_health = 500
    boss_health = 1000
    healer_info()
    while boss_health > 0 and player_health > 0:
        print()
        print(f"Tank HP: {player_health}")
        print(f"BOSS HP: {boss_health}")
        print()
        print()
        action = int(input("Attack(1) or heal the tank(2)\n"))
        if action == 1:
            boss_health = boss_health - player_hit()
            tank_dps = random.randint(100, 140)
            boss_health = boss_health - tank_dps
            print(f"The tank slammed the boss for {tank_dps}")
        elif action == 2:
            player_health = player_health + player_heal()
        else:
            print()
            print("You messed up, the boss striked the tank twice. Ouch!")
            player_health = player_health - boss_hit()
        player_health = player_health - boss_hit()

    if boss_health <= 0:
        print("Congratulations! You defeated the boss!")
    else:
        answer = input("You died, do you want to try again? yes/no\n")
        if answer == "yes":
            main()
        else:
            print("Thank you for trying out my game :)")


def main():
    """
    This is the main function. The user chooses role here
    and also check validation of the input.
    """
    print("What role would you like to play?")
    role_choice = input("Type 'tank' or 'healer' to choose.\n")
    print()
    if role_choice == "tank":
        tank()
    elif role_choice == "healer":
        healer()
    else:
        print("That is not correct, please select one of the above roles")
        main()


welcome()
main()
