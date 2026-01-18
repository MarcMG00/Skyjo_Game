class Player:
    ROWS = 3
    COLS = 4

    def __init__(self, number: int):
        self.number = number
        self.grid = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.score = 0

    # Distribute 12 Cards to player
    def deal_cards(self, deck):
        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.grid[r][c] = deck.draw()

    # Reveal Card selected
    def reveal_card(self, row: int, col: int):
        self.grid[row][col].reveal()

    # Display the Cards (in table form)
    def display(self):
        print(f"\nJugador {self.number}")
        print("   1  2  3  4")
        for i, row in enumerate(self.grid):
            row_str = " ".join(str(card) for card in row)
            print(f"{i+1} {row_str}")