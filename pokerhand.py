from hand import Hand

class PokerHand(Hand):
    def __init__(self, label: str):
        super().__init__(label)

    def deal_hand(self,num_cards):
        pass

    def evaluate_hand(self) -> str:
        return "Evaluation of Poker Hand"