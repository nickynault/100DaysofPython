import art
import time
from game_data import data
import random


def randomChoice():
    random_item = random.choice(data)
    name = random_item['name']
    follower_count = random_item['follower_count']
    description = random_item['description']
    country = random_item['country']
    return name, follower_count, description, country


def game():
    score = 0
    nameA, followsA, descA, countryA = randomChoice()

    while True:
        nameB, followsB, descB, countryB = randomChoice()

        print(f"Compare A: {nameA}, {descA}, from {countryA}.")
        print(art.vs)
        print(f"Against B: {nameB}, {descB}, from {countryB}.")

        answer = input("Who has more followers? Type 'A' of 'B': ").lower()

        winner = 'a' if followsA > followsB else 'b'

        if answer == winner:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            try_again = input("Try again? 'y' or 'n': ")
            if try_again == 'y':
                game()
            else:
                break

        if followsA < followsB:
            nameA, followsA, descA, countryA = nameB, followsB, descB, countryB

        time.sleep(1)
        print("\033[F\033[K", end='')


print(art.logo)
print("Welcome to the Higher Lower Game!")
print("You'll need to determine which of the two has more followers.")
choice = input("Ready? 'y': ")
if choice == 'y':
    game()
