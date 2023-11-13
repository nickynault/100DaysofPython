import art
import random


def draw_cards(types, values, num_cards=2):
    cards = []
    for _ in range(num_cards):
        card_type = random.choice(types)
        card_value = random.choice(list(values.keys()))
        card = f"{card_value} of {card_type}"
        cards.append(card)
    return cards


def draw_additional_card(types, values, hand):
    card_type = random.choice(types)
    card_value = random.choice(list(values.keys()))
    card = f"{card_value} of {card_type}"
    hand.append(card)
    return hand


def display_cards(player_name, cards):
    print(f"{player_name} cards are: {' and the '.join(cards)}.")


def calculate_score(hand, values):
    total_value = sum(values[card.split()[0]] for card in hand)
    has_blackjack = total_value == 21

    if total_value > 21 and "Ace" in hand:
        total_value -= 10

    return total_value, has_blackjack


choice = input("Welcome to Blackjack! Play a game? 'y' or 'n':\n")
print(art.logo)

cards_types = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


def game():
    global choice
    print("Let's Play!")
    # Draw cards for CPU and player
    CPU_hand = draw_cards(cards_types, cards_values)
    player_hand = draw_cards(cards_types, cards_values)

    # Display cards
    display_cards("Your", player_hand)

    # Grab score, has_blackjack, and ace_value
    CPU_score, cpu_has_blackjack = calculate_score(CPU_hand, cards_values)
    player_score, player_has_blackjack = calculate_score(player_hand, cards_values)

    # Show scores
    print(f"\nThe CPU's current score is: {CPU_score}")
    print(f"Your current score is: {player_score}")

    # Check for initial blackjack
    if cpu_has_blackjack:
        print("The CPU has a blackjack! You lose!")
        choice = input("Play again? 'y' or 'n': \n")
    elif player_has_blackjack:
        print("You have a blackjack! You win!")
        choice = input("Play again? 'y' or 'n': \n")
    else:
        print("No blackjack this round.\n")

    # Show CPU first card
    print(f"The CPU's first card is the: {CPU_hand[0]}")

    # Keep it going
    draw = "y"
    while draw == 'y':
        draw = input("Do you want to draw another card? 'y' or 'n': \n")
        player_hand = draw_additional_card(cards_types, cards_values, player_hand)
        display_cards("Your", player_hand)

        # Check for player bust
        player_score, player_has_blackjack = calculate_score(player_hand, cards_values)
        if player_score > 21:
            print("You went over 21. You lose!")
            choice = input("Play again? 'y' or 'n': \n")
            return

    # CPU's turn to draw additional cards
    while CPU_score < 17:
        CPU_hand = draw_additional_card(cards_types, cards_values, CPU_hand)
        CPU_score, cpu_has_blackjack = calculate_score(CPU_hand, cards_values)
        print("The CPU draws another card.")

        # Check for CPU bust
        if CPU_score > 21:
            print("The CPU went over 21. You win!")
            choice = input("Play again? 'y' or 'n': \n")
            return

    # Compare scores and determine the winner
    if player_score <= 21 and (player_score > CPU_score or CPU_score > 21):
        print("You win!")
    elif CPU_score <= 21 and (CPU_score > player_score or player_score > 21):
        print("The CPU wins. You lose!")
    else:
        print("It's a tie!")


while choice == "y":
    game()
