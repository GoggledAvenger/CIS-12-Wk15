from random import shuffle
from card import Card

class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards else Deck.make_cards()

    #inline for loop using list comprehension
    @staticmethod
    def make_cards():
        return [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]

    #nested for loop
    @staticmethod
    def make_cards_nl():
        cards = []
        for suit in range(4):
            for rank in range(1,14):
                cards.append(Card(suit, rank))
        return cards

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

    def take_card(self) -> Card:
        return self.cards.pop() if self.cards else None

    def put_card(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, other: 'Deck', num: int):
        for _ in range(num):
            other.put_card(self.take_card())