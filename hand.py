from deck import Deck
from card import Card

class Hand(Deck):
    def __init__(self, label: str):
        super().__init__()
        self.label = label
        self.cards = []

    def add_card(self, card: Card):
        self.put_card(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def __str__(self):
        return f"{self.label}: " + ", ".join(str(card) for card in self.cards)

#testing
deck = Deck()
deck.shuffle()
hands = [Hand('Trevor'),Hand('Toshi'),Hand('Cody')]
for hand in hands:
    deck.move_cards(hand,5)
    print(f"{hand.label}'s hand is {hand}")

