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

# turns hand gestures into list
hand_list = [rock, paper, scissors]

# user chooses a number from the list
user_choice = int(input("Choose your option: Rock (0), Paper (1), Scissors (2)\n"))
# if choice is not 0-2 game stops
if user_choice not in [0, 1, 2]:
    print("Invalid choice, please try again (0, 1, 2)")
else:
    # prints user's choice by using input for index of list
    print("Player chose:", hand_list[user_choice])

    # random int for computer
    computer_choice = random.randint(0, 2)
    # prints computer's choice by using random int for index of list
    print("Computer chose:", hand_list[computer_choice])

    if user_choice == 0 and computer_choice == 2: # rock beats scissors
        print("User wins!")
    elif user_choice == 1 and computer_choice == 0: # paper beats rock
        print("User wins!")
    elif user_choice == 2 and computer_choice == 1: # scissors beats paper
        print("User wins!")
    elif user_choice == computer_choice or computer_choice == user_choice: # ties if same
        print("It's a tie!")
    else:
        print("Computer wins!") # if user didn't win or tie then computer wins anything else
