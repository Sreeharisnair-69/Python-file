'''
Name: Sreehari Sreekumar Nair
Date: 3 Dec 2024
Purpose: Write a program to play a sticks game in which there are 16 sticks.
    Two players take turns to play the game. Each player picks one set of sticks
    (needn’t be adjacent) during his turn. A set contains 1, 2, or 3 sticks.
    The player who takes the last stick is the loser.
    The number of sticks in the set is to be input.
'''

def sticks_game():
    player_one = input("Who is player one: ")
    player_two = input("Who is player two: ")
    current_player = 0
    total_number_of_sticks = 16
    print("Total number of sticks is 16")

    while total_number_of_sticks>0:
        current_player = player_one
        player_one_sticks = int(input(f"{player_one} pick either 1, 2 or 3 sticks: "))
        if player_one_sticks > 3 or player_one_sticks < 1:
            print("Invalid number, pick 1, 2 or 3")
        else:
            number_of_sticks = total_number_of_sticks - player_one_sticks
            print(f"There are now {number_of_sticks} sticks")
            total_number_of_sticks = number_of_sticks

        current_player = player_two
        player_two_sticks = int(input(f"{player_two} pick either 1, 2 or 3 sticks: "))
        if player_two_sticks > 3 or player_two_sticks < 1:
            print("Invalid number, pick 1, 2 or 3")
        else:
            number_of_sticks = total_number_of_sticks - player_two_sticks
            print(f"There are now {number_of_sticks} sticks")
            total_number_of_sticks = number_of_sticks

        if number_of_sticks <= 0:
            print(f"{current_player}, you lose!")
            break

sticks_game()

