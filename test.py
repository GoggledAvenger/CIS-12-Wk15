from deck import Deck
from hand import Hand

# Usage
deck = Deck()
hand = Hand("Player 1")
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())

print(hand)  # Output: Player 1's Hand: Random Card 1, Random Card 2