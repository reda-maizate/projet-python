import random


class Dice:
    def __init__(self, nb_of_sides=6):
        self.nb_of_sides = nb_of_sides
        self.__value = self.roll()

    def get_value(self):
        return self.__value

    #def __str__(self):
    #    return str(self.__value)

    value = property(get_value)

    def roll(self):
        """
        Roll a dice.
        Parameter:
        - nb_of_sides -- by default 6, like a real dice.
        Return:
        - A random value between 1 and nb_of_sides.
        """
        self.__value = random.randint(1, self.nb_of_sides)
        return self.__value
