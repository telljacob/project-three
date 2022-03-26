# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def tank_game():
    print("Hello tanks")

def healer_game():
    print("Hello healers")

def dps_game():
    print("Hello dps")

def main():
    player_health = 100
    boss_health = 100
    
    print("CHAMPION! I have been waiting for you, we need help slaying this vile beast! We are here to support you in any way we can. We can adapt to your preferred role, how do you wish to handle this?")
    
    role_choice = input(print("Which role would you like to play for this encounter: "))
    print(f"A {role_choice}, fantastic choice, just what we need!")