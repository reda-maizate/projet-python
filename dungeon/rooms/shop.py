from characters.hero import Hero
from dungeon.rooms.room import Room


class Shop(Room):
    def __init__(self, hero : Hero):
        from dungeon.exits import Exits

        self.hero = Hero
        commands = {
            "deposer": self.deposit,
            "retirer": self.withdraw,
            "ameliorer": self.upgrade,
        }
        super().__init__("Boutique", "Faites vos achats et déposez de l'argent", exits=[Exits.SHOP, Exits.NEXT_ROOM],
                         commands=commands)

    def deposit(self):
        ...

    def withdraw(self):
        ...

    def upgrade(self):
        ...

    # def __str__(self):
    #     return super.__str__(self)
