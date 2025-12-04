# blackjack

import random

deck = {}
available_card_ids = []

card_categories = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_types = {
    "Ace": 11,
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
}

types = {
    "dict": type({}),
    "list": type([]),
    "tuple": type(()),
}
def deep_clone(whatever : dict | list | tuple):
    whatever_type = type(whatever)

    if whatever_type == types["dict"]:
        result = {}
        for k, v in whatever.items():
            v_type = type(v)
            if v_type == types["dict"] or v_type == types["list"] or v_type == types["tuple"]:
                v = deep_clone(v)
            if not v:
                continue
            result[k] = v

        return result
    elif whatever_type == types["list"]:
        result = []
        for v in whatever:
            v_type = type(v)
            if v_type == types["dict"] or v_type == types["list"] or v_type == types["tuple"]:
                v = deep_clone(v)
            if not v:
                continue
            result.append(v)

        return result
    else:
        print("\n>\t\t\\/\t\t<"*6 + "\n" + "Warning: Can't Deep Clone Tuples!" + "\n>\t\t/\\\t\t<"*6)
        return None

# load deck
for category in card_categories:
    #cloned_card_types = deep_clone(card_types)
    deck[category] = deep_clone(card_types) # cloned_card_types
    # call following by initial refresh_deck()
    #for k in cloned_card_types:
    #    available_card_ids.append(f"{category} {k}")

def refresh_deck(hand1=None, hand2=None):
    if hand1 is None:
        hand1 = []
    if hand2 is None:
        hand2 = []
    
    available_card_ids.clear()

    handed_cards = {}
    for v in hand1:
        handed_cards[f"{v["category"]} {v["name"]}"] = True
    for v in hand2:
        handed_cards[f"{v["category"]} {v["name"]}"] = True

    for category in card_categories:
        for k in deck[category]:
            key = f"{category} {k}"
            if handed_cards.get(key):
                continue # card already handed out
            available_card_ids.append(key)
    
    random.shuffle(available_card_ids)
refresh_deck()

def deal_card(user_hand=None, computer_hand=None):
    if user_hand is None:
        user_hand = []
    if computer_hand is None:
        computer_hand = []
    
    if len(available_card_ids) < 1:
        refresh_deck(user_hand, computer_hand)
    
    card_id = available_card_ids.pop()
    category, name = card_id.split(" ")

    return {
        "category": category,
        "name": name,
        "value": deck[category][name],
    }

def calculate_score(hand):
    hand_sum = 0
    aces = 0

    for v in hand:
        hand_sum += v["value"]
        if v["value"] == 11:
            aces += 1

    if len(hand) == 2 and hand_sum == 21:  
        return 0 # use 0 to represent blackjack

    # Aces handling
    while aces > 0 and hand_sum > 21:
        hand_sum -= 10
        aces -= 1
    
    return hand_sum


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def stringify_hand(hand):
    entries = []

    for v in hand:
        entries.append(f"{v["name"]} {v["category"]}")

    return f"Total = {calculate_score(hand)}\n>\t" + "\n>\t".join(entries)

def play_game():
    user_hand = []
    computer_hand = []

    for _ in range(2):
        user_hand.append(deal_card(user_hand, computer_hand))
        computer_hand.append(deal_card(user_hand, computer_hand))

    user_playing = True
    game_over = False

    while user_playing and not game_over:
        print("\n"*30)
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your hand: {stringify_hand(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]["name"]} {computer_hand[0]["category"]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            hit = input("Type 'y' to hit, 'n' to stand: ").strip().lower()
            if hit == "y":
                user_hand.append(deal_card())
            else:
                user_playing = False
    
    while computer_score != 0 and computer_score < 17 and not game_over:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand:{stringify_hand(user_hand)}")
    print(f"Computer final hand: {stringify_hand(computer_hand)}")
    print(compare(user_score, computer_score))


while input("Play blackjack? (y/n): ").strip().lower() == "y":
    play_game()