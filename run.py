"""
high level support for doing this and that.
"""


def welcome():
    """
        We introduce the user to the game and let the user choose role.
        We return to this function every time we want the game to reset.
    """
    print("CHAMPION! I have been waiting for you!")
    print("We need help slaying this beast! What role would you like to play?")


def tank_game():
    """
    This function implements all your abilities as a tank player
    """
    print("Hello tanks")


def healer_game():
    """
    This function implements all your abilities as a healer player
    """
    print("Hello healers")


def dps_game():
    """
    This function implements all your abilities as a dps player
    """
    print("Hello dps")


def main():
    """
    This is the main function
    """
    # player_health = 100
    # boss_health = 100
    print("Would you like to be a tank, healer or dps?")
    role_choice = input(print("Type 'tank', 'healer' or 'dps' to choose."))
    print(f"Fantastic choice, a {role_choice} is just what we need!")
    if role_choice == "tank":
        tank_game()
    elif role_choice == "healer":
        healer_game()
    elif role_choice == "dps":
        dps_game()
    else:
        print("Please input a valid role")


main()
