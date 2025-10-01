from die import Die
from player import Player
import check_input

def take_turn(player: Player):
    player.roll_dice()
    print(player)
    if(player.has_three_of_a_kind()):
        print("You got 3 of a kind!")
    elif(player.has_pair()):
        print("You got a pair!")
    elif(player.has_series()):
        print("You got series of 3")
    else:
        print("Aww. Too bad.")
    print(f"Score = {player.points}")

def main():
    player = Player()
    print("-Yahtzee-")

    play = True
    while play:
        take_turn(player)
        if(not check_input.get_yes_no("Play again? (Y/N): ")):
            print("Game Over.")
            print(f"Final Score = {player.points}")
            break


if __name__ == "__main__":
    main()