from deck import Deck
from hand import Hand

class PokerDeck(Deck):
    def __init__(self):
        super().__init__()
        self.shuffle()

    def deal_hand(self, hand, num_cards):
        return self.move_cards(hand, num_cards)

# Usage
deck = PokerDeck()

hands = [Hand('Trevor'),Hand('Toshi'),Hand('Cody')]
for hand in hands:
    deck.move_cards(hand,5)
    print(f"{hand.label}'s hand is {hand}")
