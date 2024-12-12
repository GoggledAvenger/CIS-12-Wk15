from hand import Hand

class BridgeHand(Hand):
    def __init__(self, label: str):
        super().__init__(label)

    def evaluate_hand(self) -> dict:
        return "Evaluation of Bridge Hand"