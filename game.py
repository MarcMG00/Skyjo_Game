from deck import Deck
from player import Player

class Game:
    def __init__(self, num_players: int):
        self.deck = Deck()
        self.players = [Player(i + 1) for i in range(num_players)]

    def setup(self):
        for player in self.players:
            player.deal_cards(self.deck)

        # First rule: each player reveals 2 Cards
        for player in self.players:
            player.reveal_card(0, 0)
            player.reveal_card(1, 1)
        
        self.determine_starting_player()

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