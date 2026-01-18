from game import Game

def main():
    num_players = int(input("Número de jugadores: "))
    game = Game(num_players)
    game.setup()
    game.display()

if __name__ == "__main__":
    main()