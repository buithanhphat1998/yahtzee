""" CECS 277 – Lab 6 – Class Relationships
10/01/2025
    Group 4
    Student 1: Thanh Phat Bui
    Student 2: Ha Gia Bao Hoang
Description: Yahtzee: Create a dice game that awards the user points for a pair, three-of-a-kind, or a series."""
from die import Die
from player import Player
import check_input

def take_turn(player: Player):
    # Roll all dice
    player.roll_dice()
    # Show dice values.
    print(player)
    # Check scoring
    if(player.has_three_of_a_kind()):
        print("You got 3 of a kind!")
    elif(player.has_pair()):
        print("You got a pair!")
    elif(player.has_series()):
        print("You got series of 3")
    else:
        print("Aww. Too bad.")
    # Show current score after the turn.
    print(f"Score = {player.points}")

def main():
    # Create a player
    player = Player()
    print("-Yahtzee-")

    play = True
    while play:
        #round loop
        take_turn(player)
        # Ask user if they want to play again.
        if(not check_input.get_yes_no("Play again? (Y/N): ")):
            print("Game Over.")
            # Show final score
            print(f"Final Score = {player.points}")
            break


if __name__ == "__main__":
    main()