# so I was supposed to use a dictionary and then find the max bid
# however it's really much simpler to keep track of the last bid and name
# at first I though of using kv pairs of [bidAmount] = name and a list
# with all bidAmounts, and do bids[str(max(list))] to get the winner
# but since each bid is always bigger than the previous one, just override.

last_name = ""
last_bid = 0
bidding_finished = False

def bid_with_name(name):
    global last_name, last_bid
    price = int(input("Your bid: $"))

    if price <= last_bid:
        print(f"Can't bid lower or equal to max bid")
        bid_with_name(name)
        return
    
    last_name = name
    last_bid = price
    

while not bidding_finished:
    print(f"current biggest bid is ${last_bid}")
    name = input("(Leave blank to skip and end the auction)\nEnter your name: ").strip()
    if len(name) < 1:
        bidding_finished = True
        continue
    bid_with_name(name)

    more = input("Are there other bidders? (yes/no): ").strip().lower()
    if more == "no":
        bidding_finished = True
    else:
        print("\n" * 33) # clear

print(f'\nWinner is "{last_name}" with a bid of ${last_bid}!')