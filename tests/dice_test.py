from game.game_settings import *


def dice_test():
    d = Dice()
    t = Dice()
    for i in range(5):
        print(d.value)
    print(f"Compare {d} with {t} and the winner is index {d.compare(t)}")
    d.roll()
    t.roll()
    for i in range(5):
        print(d.value)
    print(f"Compare {t} with {d} and the winner is index {t.compare(d)}")

