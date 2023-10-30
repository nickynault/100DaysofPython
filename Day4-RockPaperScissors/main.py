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

print("Welcome to the rock paper scissors game!")
choice = int(input("What do you choose? Type '0' for rock, '1' for paper, and '2' for scissors.\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

choices = [0, 1, 2]
random_choice = random.randint(0, 2)
random_response = choices[random_choice]

if random_response == 0:
    print(f"The computer chose: {rock}")
elif random_response == 1:
    print(f"The computer chose: {paper}")
elif random_response == 2:
    print(f"The computer chose: {scissors}")

if choice == random_response:
    print("Darn, you've tied! Try again?")
elif (choice == 0 and random_response == 1) or (choice == 1 and random_response == 2) or (choice == 2 and random_response == 0):
    print("You lost! Try again?")
elif (choice == 0 and random_response == 2) or (choice == 1 and random_response == 0) or (choice == 2 and random_response == 1):
    print("You win!")

# Teacher's Solution
the_teacher_response = '''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
'''
