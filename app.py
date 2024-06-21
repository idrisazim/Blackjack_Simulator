import random
CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': (1, 11)}

def build_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [(rank, suit) for rank in ranks for suit in suits] * 4

def get_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        rank, _ = card
        if rank == 'A':
            aces = aces + 1
            total = total + 11
        else:
            total = total + CARDS[rank]

    while total > 21 and aces:
        total = total - 10
        aces = aces - 1

    return total

def draw_card(deck):
    return deck.pop()

def print_hand(player, hand):
    hand_description = ', '.join(f"{rank} of {suit}" for rank, suit in hand)
    value = get_hand(hand)
    print(f"{player}'s hand: {hand_description} (Value: {value})")

def blackjack():
    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2: ")

    deck = build_deck()
    random.shuffle(deck)

    scores = {player1: 0, player2: 0, 'Dealer': 0}
    round_count = 0

    while len(deck) >= 6:  
        round_count = round_count + 1
        player1_hand = []
        player2_hand = []
        dealer_hand = []

        for _ in range(2):
            player1_hand.append(draw_card(deck))
            player2_hand.append(draw_card(deck))
            dealer_hand.append(draw_card(deck))

        while get_hand(player1_hand) < 17:
            player1_hand.append(draw_card(deck))
        while get_hand(player2_hand) < 17:
            player2_hand.append(draw_card(deck))
        while get_hand(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))

        print("\nFinal hands:")
        print_hand(player1, player1_hand)
        print_hand(player2, player2_hand)
        print_hand('Dealer', dealer_hand)
        player1_value = get_hand(player1_hand)
        player2_value = get_hand(player2_hand)
        dealer_value = get_hand(dealer_hand)
        winners = []
        highest_value = 0
        fewest_cards = float('inf')

        for player, value, hand in [(player1, player1_value, player1_hand), (player2, player2_value, player2_hand), ('Dealer', dealer_value, dealer_hand)]:
            if value <= 21 and (value > highest_value or (value == highest_value and len(hand) < fewest_cards)):
                winners = [player]
                highest_value = value
                fewest_cards = len(hand)
            elif value == highest_value and len(hand) == fewest_cards:
                winners.append(player)

        print("\nAnd the moment of truth:")
        if len(winners) == 1:
            winner = winners[0]
            print(f"{winner} wins this round!")
            scores[winner] += 1
        else:
            print(f"too bad it's a tie between: {', '.join(winners)}")

        print(f"Scores: {scores}")

    print("\nThat's it!")
    print(f"Total rounds: {round_count}")
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    print("Final scores:")
    for player, score in sorted_scores:
        print(f"{player}: {score}")

if __name__ == "__main__":
    blackjack()
