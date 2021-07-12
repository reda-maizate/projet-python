from game.game_settings import *


def dice_test():
    d = Dice(20)
    t = Dice(20)
    for i in range(5):
        print(d.get_value())
    print(f"Compare {d.get_value()} with {t.get_value()} and the winner is index {d.compare(t)}")
    d.roll()
    t.roll()
    for i in range(5):
        print(d.get_value())
    print(f"Compare {t.get_value()} with {d.get_value()} and the winner is index {t.compare(d)}")

