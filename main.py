import Language
from utils import menu
user_choice = menu()
from game.game import Game

if __name__ == "__main__":
    Language.loadDialogs()
    Game().run()
