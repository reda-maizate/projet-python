from characters.hero import Hero
from dungeon.exits import Exits
from dungeon.rooms.room import *


class Shop(Room):
    def __init__(self, hero: Hero):

        commands = {
            "faire plus mal": self.upgrade_weapon,
            "prendre moins cher": self.upgrade_armor,
        }
        super().__init__("Boutique", "Faites vos achats et déposez de l'argent", exits=[Exits.HOME, Exits.NEXT_ROOM],
                         commands=commands, hero=hero)
        # print("une bombe sous vos pieds explose, vous mourrez")
        # hero.health = 0

    def upgrade_weapon(self):
        if self.hero.gold >= 25:
            if self.hero.force >= 70:
                print("Zerhma tu forces chacal")
                return
            print("level up de l'épée\nAttention la patate du Sheitan")
            self.hero.force += 10
            self.hero.gold -= 25
        else:
            print("déso t'as pas une thune")

    def upgrade_armor(self):
        if self.hero.gold >= 25 :
            if self.hero.armor >= 70:
                print("Zerhma tu forces chacal")
                return
            self.hero.armor += 10
            self.hero.gold -= 25
            print("level up de l'armure")
        else:
            print("déso t'as pas une thune")
