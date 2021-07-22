import random

from characters.hero import Hero
from characters.monster import Monster
from dungeon.exits import Exits
from game.game_settings import Dice
from dungeon.rooms.room import *


def loop(game=None):
    while True:
        room = Room()

        room.name = "CAVE SOMBRE"
        opennessRoll = Dice(3).get_value()
        if opennessRoll == 0:
            openness = "un labyrinthe sombre et exigu où il faut se faufiler entre tous les interstices de la roche"
        elif opennessRoll == 1:
            openness = "pas trop difficile de se faufiler, bien qu'il soit difficile de voir devant soi"
        elif opennessRoll == 2:
            openness = "un long couloir couvert de roches et de cristaux"
        else:
            openness = "une géode massive et ouverte à l'intérieur de laquelle vous vous tenez"

        wetnessRoll = Dice(3).get_value()
        if wetnessRoll == 0:
            wetness = "l'os sec en entendant le bruit de vos talons contre la roche dure en dessous"
        elif wetnessRoll == 1:
            wetness = "un peu humide car vous sentez le moût et la moisissure dans l'air"
        elif wetnessRoll == 2:
            wetness = "humide comme vous voyez l'eau s'infiltrer à travers les murs des grottes"
        else:
            wetness = "mouillé en pataugeant dans l'eau cristalline des grottes qui descend jusqu'aux chevilles"

        exitRoll = Dice(3).get_value()
        if exitRoll == 0:
            room.exits.append("nord")
        elif exitRoll == 1:
            room.exits.append("ouest")
        elif exitRoll == 2:
            room.exits.append("sud")
        else:
            room.exits.append("est")

        room.description = "Cette partie de la grotte est à {0} et {1}.\nSortie: {2}".format(openness, wetness,
                                                                                             ", ".join(room.exits))

        # Crystal Roll
        crystalRoll = Dice().get_value()
        if not crystalRoll:
            # The logic is really reversed
            # Think: if crystal
            room.description += "\nIl y a un cristal blanc brillant ici dans la pièce. La rumeur dit que si vous touchez un de ces cristaux, il vous guérira complètement, mais il prendra aussi le contrôle de votre esprit et vous fera rentrer chez vous en somnambule.\n\n"

            room.cmds = {"toucher cristal": game.warpHome,
                         "attraper cristal": game.warpHome,
                         "tc": game.warpHome()
                         }

        numMonster = Dice(3).get_value()
        # if numMonster == 0:
        #     pass
        # elif numMonster == 1:
        #     room.monsters.append(Monster())
        # elif numMonster == 2:
        #     room.monsters.append(Monster())
        # else:
        #     room.monsters.append(Monster())
        #     room.monsters.append(Monster())
        for _ in range(numMonster):
            room.monsters.append(Monster())

        yield room


class Dungeon(Room):
    def __init__(self, hero: Hero):
        super().__init__(hero)
        self.exits = [Exits.NEXT_ROOM]

        can_tp_home = random.random() >= 0.5
        if can_tp_home:
            self.exits.append(Exits.HOME)
