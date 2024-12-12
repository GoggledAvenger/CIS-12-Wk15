class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank_names[self.rank]} of {self.suit_names[self.suit]}"

    def __eq__(self, other: 'Card') -> bool:
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: 'Card') -> bool:
        return self.to_tuple() < other.to_tuple()

    def __le__(self, other: 'Card') -> bool:  # Example of using tuples directly
        return (self.suit, self.rank) <= (other.suit, other.rank)

    def to_tuple(self) -> tuple:
        return self.suit, self.rank