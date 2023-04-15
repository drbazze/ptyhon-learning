import random

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

print("Welcome to the Rock, Paper, Scissors game!\nAre you ready to beat me?")

user_choice = int(
    input('''
Pick one from bellow:
1 - Rock
2 - Paper
3 - Scissors
'''))

if user_choice < 1 or user_choice > 3:
    print("You selected an invalid option. Game over.")
else:
    computer_choice = random.randint(0, 2)

    action_names = ["Rock", "Paper", "Scissors"]
    action_graphics = [rock, paper, scissors]

    #Store the selected actions for the messages
    user_action = action_names[user_choice - 1]
    computer_action = action_names[computer_choice]

    #Game evaluation matrix rows are the computer chose whereas the columns are the user's
    #          Rock | Paper | Scissors
    #Rock     [Tie    Win       Lose  ]
    #Paper    [Lose   Tie       Win   ]
    #Scissors [Win    Lose      Tie   ]
    #
    #Matrix values:
    #-1 = Lose
    #0 = Tie
    #1 = Win

    game_evaluation_matrix = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

    #Show the selected action graphics
    print(
        f"\nPlayer is selected {user_action} {action_graphics[user_choice-1]}\n"
    )
    print(
        f"Computer is selected {computer_action}{action_graphics[computer_choice]}\n"
    )

    #Evaluate the game
    if game_evaluation_matrix[computer_choice][user_choice - 1] == -1:
        print(f"{computer_action} beats {user_action}. You lose.")
    elif game_evaluation_matrix[computer_choice][user_choice - 1] == 1:
        print(f"{user_action} beats {computer_action}. You win!")
    else:
        print(f"Both selected the same {user_action}. It's a tie!")
