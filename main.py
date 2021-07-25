import Language
from menu import menu
user_choice = menu()
Language.loadDialogs(user_choice)
from game.game import Game

if __name__ == "__main__":
    Game().run()
