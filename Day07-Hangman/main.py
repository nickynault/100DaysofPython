import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
lives = 6
end = False
print(logo)

display = []
for letter in chosen_word:
    display.append("_")

while not end:
    guess = input("Guess a letter: \n").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"\n{guess} is not in the chosen word. Careful!\n")
        lives -= 1
        if lives == 0:
            end = True
            print(f"\nYou lose. The word was {chosen_word}\n")

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end = True
        print("\nYou win!")
