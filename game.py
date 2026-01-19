from deck import Deck
from player import Player

class Game:
    def __init__(self, num_players: int):
        self.deck = Deck()
        self.players = [Player(i + 1) for i in range(num_players)]
        self.current_player_index = 0

    def setup(self):
        for player in self.players:
            player.deal_cards(self.deck)

        # First rule: each player reveals 2 Cards
        for player in self.players:
            player.reveal_card(0, 0)
            player.reveal_card(1, 1)
        
        self.determine_starting_player()
        self.current_player_index = 0  # after reordering players

    # Show player's Cards
    def display(self):
        for player in self.players:
            player.display()

    # Determine order to play the game
    def determine_starting_player(self):
        # Calculate initial sum of every player
        sums = []
        for player in self.players:
            sums.append((player, player.initial_revealed_sum()))

        # Select player with highest result
        starting_player, max_sum = max(sums, key=lambda x: x[1])

        print(f"\nEmpieza el Jugador {starting_player.number} (suma inicial de : {max_sum})")

        self.reorder_players(starting_player)

    # Reordenate player's list
    def reorder_players(self, starting_player):
        index = self.players.index(starting_player)
        self.players = self.players[index:] + self.players[:index]

    # Start turns
    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"\nTurno del Jugador {current_player.number}")

        # Show Cards of current player
        current_player.display()

        while True:
            try:
                row = int(input("Elige fila (1-3): ")) - 1
                column = int(input("Elige columna (1-4): ")) - 1

                # Check range
                if row not in range(3) or column not in range(4):
                    print("Posición fuera de rango.")
                    continue

                card = current_player.grid[row][column]
                if card.revealed:
                    print("Esta carta ya está revelada.")
                    continue

                card.reveal()
                print(f"Has revelado la carta: {card.value}")
                break

            except ValueError:
                print("Entrada inválida. Usa números.")
                continue

        # Show again all player's Cards
        self.display()

        # Next player
        self.next_player()

    # Pass to next player (next index)
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)