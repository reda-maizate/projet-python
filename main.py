from game.game import Game
from utils import loadDialogs, menu

# todo ask for language

if __name__ == "__main__":
    user_choice = menu()
    loadDialogs(user_choice)
    Game().run()
