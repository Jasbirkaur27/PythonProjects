
bid={}
continue_biding=True

def find_highest(bidding_dict):
    winner=""
    highest_bid=0
    for bidder in bidding_dict:
        bid_amt=bidding_dict[bidder]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bidder
    print(f"The highest bid is of ${highest_bid} by {winner}.")        

while continue_biding:
    name=input("What is your name? ")
    price=int(input("What is your bid? $"))
    should_continue=input("Are there any other bidders Type 'yes' or 'no' ").lower()
    bid[name]=price
    if should_continue=='no':
        continue_biding=False
        find_highest(bid)
        #print(max(bid,key=bid.get))
    elif should_continue=='yes':
        print("\n" *30)    

