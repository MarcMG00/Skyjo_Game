class Card:
    def __init__(self, value: int):
        self.value = value
        self.revealed = False
        self.discarded = False

    def reveal(self):
        self.revealed = True

    def hide(self):
        self.revealed = False

    # Discard card when a column has the 3 same Cards
    def discard(self):
        self.discarded = True
        self.revealed = True  # to see it as "D"

    def __str__(self):
        if self.discarded:
            return " D"
        if self.revealed:
            return f"{self.value:>2}"
        return " X"