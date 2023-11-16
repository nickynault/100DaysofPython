import random
import art


def game(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    rangeX = range(1, 100)
    answer = random.choice(rangeX)
    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess < answer:
            print("\nToo low.")
            attempts -= 1
        elif guess > answer:
            print("\nToo high.")
            attempts -= 1
        elif guess == answer:
            print(f"You got it! The answer was {answer}.")
            exit()

        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")

    print("\nUh oh... You're out of attempts. You lose!")
    exit()


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.\n").lower()

if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)
