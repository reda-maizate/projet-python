import Language
from game.game import Game
from utils import menu


# todo ask for language

if __name__ == "__main__":
    user_choice = menu()
    Language.loadDialogs(user_choice)
    Game().run()
