from characters.hero import Hero
from dungeon.exits import Exits
from dungeon.rooms.room import *


class Shop(Room):
    def __init__(self, hero : Hero):

        self.hero = hero
        commands = {
            "deposer": self.deposit,
            "retirer": self.withdraw,
            "ameliorer": self.upgrade,
        }
        super().__init__("Boutique", "Faites vos achats et déposez de l'argent", exits=[Exits.HOME, Exits.NEXT_ROOM],
                         commands=commands)

    def deposit(self):
        ...

    def withdraw(self):
        ...

    def upgrade(self):
        ...