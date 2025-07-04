# project - 9 : Secret auction program

logo = '''
  _________      
 /         \      
|  SECRET   |      
|  AUCTION  |      
 \_________/       
     | |           
     | |         
    _|_|_          
   /     \        
  | LOCK  |       
  |_______|       

'''

print(logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for biddre in bidding_dictionary :
        bid_amount = bidding_dictionary[biddre]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = biddre
        
    print(f"The Winner is {winner} with a bid of $ {highest_bid}")


bids = {}
continue_bidding =True

while continue_bidding :
    name = input("What is your Name  ? : ").lower()
    price = int(input("What is Your Bid  ? : $ "))
    bids [name] = price
    should_continue = input("Are There any other bidders  ? type 'yes' or 'no' : ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 11)

