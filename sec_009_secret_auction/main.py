from art import logo
from replit import clear

print(logo)

all_bids = {}

def finding_highest_bidder(bidding_record):
    list_of_bidders = []
    bids_of_bidders = []
    for key in bidding_record:
        list_of_bidders.append(key)
        bids_of_bidders.append(bidding_record[key])
    highest_bid  = max(bids_of_bidders)
    winner = list_of_bidders[bids_of_bidders.index(highest_bid)]
    print(f"The winner is {winner} with a bid of $ {highest_bid}")

evaluate_auction = True
while evaluate_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid in $?: "))
    all_bids[name] = bid

    last_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    if not (last_bidder == "yes" or last_bidder == "no"):
        while not (last_bidder == "yes" or last_bidder == "no"):
            last_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")

    clear()
    
    if last_bidder == "no":
        finding_highest_bidder(all_bids)    
        evaluate_auction = False



