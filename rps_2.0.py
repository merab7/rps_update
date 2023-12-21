import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Initialize counts outside the play function
game_count = 0
player_count = 0
computer_count = 0
tie_game = 0

def play():
    

    pl_move = input(
        "Hello player, choose 0 for rock, 1 for paper, or 2 for scissors\n")
    computer = random.randint(0, 2)

    def start():
        global game_count, player_count, computer_count, tie_game

        def play_again():
            
            again = input("If you want to play again press Y or X for exit.\n")
            if again.lower() in ["y", "x"]:
                if again.lower() == "y":
                    return play()
                else:
                    print("Bye")
                    sys.exit()
            else:
                print(
                    "You did not press the right key. You only have 2 options: Y and X"
                )
                return play_again()

        if pl_move in ["0", "1", "2"]:
            pl_move_int = int(pl_move)

            if pl_move_int == 0 and computer == 2:
                print(
                    f"Your choice:\n{rock}\nComputer chose:\n{scissors}\nYou won "
                )
                game_count += 1
                player_count += 1

            elif pl_move_int == 1 and computer == 0:
                print(
                    f"Your choice:\n{paper}\nComputer chose:\n{rock}\nYou won "
                )
                game_count += 1
                player_count += 1

            elif pl_move_int == 2 and computer == 1:
                print(
                    f"Your choice:\n{scissors}\nComputer chose:\n{paper}\nYou won "
                )
                game_count += 1
                player_count += 1

            elif pl_move_int == computer:
                print(
                    f"Your choice: {rock if pl_move_int == 0 else paper if pl_move_int == 1 else scissors}\n"
                    f"Computer chose: {rock if computer == 0 else paper if computer == 1 else scissors}\n"
                    f"Tie game ")
                game_count += 1
                tie_game += 1
            else:
                print(
                    f"Your choice: {rock if pl_move_int == 0 else paper if pl_move_int == 1 else scissors}\n"
                    f"Computer chose: {rock if computer == 0 else paper if computer == 1 else scissors}\n"
                    f"You lost ")
                game_count += 1
                computer_count += 1

            print(
                f"Game count: {game_count}\nYour score: {player_count}\nComputer count: {computer_count}\nTie games : {tie_game}"
            )
            play_again()
        else:
            print(
                "You did not press the right key.\nYou only have 3 options: 0 for rock, 1 for paper, or 2 for scissors "
            )
            return play()

    start()

# Call the play function
play()
