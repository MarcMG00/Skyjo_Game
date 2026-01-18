import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self._build()
        self.shuffle()

    # Set initial deck of the game
    def _build(self):
        # Original deck for Skyjo game
        values = (
            [-2] * 3 +
            [-1] * 7 +
            [0] * 11 +
            [1] * 7 +
            [2] * 7 +
            [3] * 7 +
            [4] * 7 +
            [5] * 7 +
            [6] * 7 +
            [7] * 7 +
            [8] * 7 +
            [9] * 7 +
            [10] * 7 +
            [11] * 7 +
            [12] * 7
        )

        for v in values:
            self.cards.append(Card(v))

    # Shuffle deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Get Card from above of the deck
    def draw(self):
        return self.cards.pop()