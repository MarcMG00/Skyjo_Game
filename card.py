class Card:
    def __init__(self, value: int):
        self.value = value
        self.revealed = False

    def reveal(self):
        self.revealed = True

    def hide(self):
        self.revealed = False

    def __str__(self):
        if self.revealed:
            return f"{self.value:>2}"
        else:
            return " X"