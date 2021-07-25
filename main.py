from game.game import Game
from utils import loadDialogs

# todo ask for language

if __name__ == "__main__":
    loadDialogs()
    Game().run()
