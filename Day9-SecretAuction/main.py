import art


def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        x = int(bid_record[bidder])
        if x > highest_bid:
            highest_bid = x
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}!")


print(art.logo)
print("Welcome to the Secret Auction!\n")
bids_and_names = {}
continue_auction = True

while continue_auction:
    name = input("What is your preferred name?\n")
    bid = input("What is your bid?\n")
    bids_and_names[name] = bid
    choice = input("Are there other users who want to bid? (Yes or No)\n").lower()
    if choice == "yes":
        continue_auction = True
    elif choice == "no":
        continue_auction = False
        highest_bidder(bids_and_names)
