from deck import Deck
from player import Player

class Game:
    def __init__(self, num_players: int):
        self.deck = Deck()
        self.discard_pile = []
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

         # Initial Card from descart pile
        first_discard = self.deck.draw()
        first_discard.reveal()
        self.discard_pile.append(first_discard)

        print(f"\nCarta inicial del descarte: {first_discard.value}")

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

        top_discard = self.discard_pile[-1]
        print(f"Carta visible del descarte: {top_discard.value}")

        while True:
            print("\nElige una acción:")
            print("1 - Girar una carta propia")
            print("2 - Cambiar una carta con el descarte")
            print("3 - Robar carta del mazo")

            choice = input("Opción: ")

            if choice == "1":
                self.flip_own_card(current_player)
                break
            elif choice == "2":
                self.swap_with_discard(current_player)
                break
            elif choice == "3":
                self.draw_from_deck_action(current_player)
                break
            else:
                print("Opción inválida.")

        # Show again all player's Cards
        self.display()

        # Next player
        self.next_player()

    # Option 1 - Flip one of Player's Card
    def flip_own_card(self, player):
        while True:
            try:
                row = int(input("Fila (1-3): ")) - 1
                col = int(input("Columna (1-4): ")) - 1

                if row not in range(3) or col not in range(4):
                    print("Fuera de rango.")
                    continue

                card = player.grid[row][col]
                if card.revealed:
                    print("Carta ya revelada.")
                    continue

                card.reveal()
                print(f"Carta revelada: {card.value}")
                return

            except ValueError:
                print("Entrada inválida.")

    # Option 2 - Swap a Card from descarted deck
    def swap_with_discard(self, player):
        discard_card = self.draw_from_discard()

        row, col = self.ask_position(player)
        player_card = player.grid[row][col]

        self.add_to_discard(player_card)
        discard_card.reveal()
        player.grid[row][col] = discard_card

        print(f"Cambiada por carta {discard_card.value}")

    # Option 3 - Draw a Card from principal deck and do something
    def draw_from_deck_action(self, player):
        card = self.draw_from_deck()
        card.reveal()

        print(f"Has robado: {card.value}")

        while True:
            choice = input("1 - Cambiarla | 2 - Descartarla: ")

            if choice == "1":
                row, col = self.ask_position(player)
                old_card = player.grid[row][col]

                self.add_to_discard(old_card)
                player.grid[row][col] = card
                return

            elif choice == "2":
                self.add_to_discard(card)
                return

            else:
                print("Entrada inválida.")

    # Get Card from player to exchange
    def ask_position(self, player):
        while True:
            try:
                row = int(input("Fila (1-3): ")) - 1
                col = int(input("Columna (1-4): ")) - 1

                if row in range(3) and col in range(4):
                    return row, col
                else:
                    print("Fuera de rango.")

            except ValueError:
                print("Entrada inválida.")

    # Pass to next player (next index)
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    # Get Card from above of principal deck
    def draw_from_deck(self):
        self.reshuffle_if_needed()
        return self.deck.draw()

    # Get Card from above of discarted Cards
    def draw_from_discard(self):
        if not self.discard_pile:
            return None
        return self.discard_pile.pop()

    # Put Card to discard on discarted pile
    def add_to_discard(self, card):
        card.reveal()
        self.discard_pile.append(card)

    # If no more Cards on principal deck, set new deck with discarted pile (ans shuffle it)
    def reshuffle_if_needed(self):
        if not self.deck.cards:
            print("Rebarajando descartes...")

            # Leave only last Card from discarted deck
            top_discard = self.discard_pile.pop()

            # Hide all Cards from discarted pile
            for card in self.discard_pile:
                card.hide()

            self.deck.cards = self.discard_pile
            self.discard_pile = [top_discard] # puts last Card from discarted deck
            self.deck.shuffle()