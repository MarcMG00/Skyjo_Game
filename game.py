from deck import Deck
from player import Player

class Game:
    def __init__(self, num_players: int):
        self.deck = Deck()
        self.players = [Player(i + 1) for i in range(num_players)]

    def setup(self):
        for player in self.players:
            player.deal_cards(self.deck)

        # Regla inicial Skyjo: cada jugador revela 2 cartas
        for player in self.players:
            player.reveal_card(0, 0)
            player.reveal_card(1, 1)

    def display(self):
        for player in self.players:
            player.display()