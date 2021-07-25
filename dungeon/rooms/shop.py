from characters.hero import Hero
from dungeon.exits import Exits
from dungeon.rooms.room import *

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["game"]["shop"]


class Shop(Room):
    def __init__(self, hero: Hero):

        commands = {
            page_dialog["armure"]: self.upgrade_weapon,
            page_dialog["arme"]: self.upgrade_armor,
        }
        super().__init__(page_dialog["name"],
                         page_dialog["description"],
                         exits=[Exits.HOME, Exits.NEXT_ROOM],
                         commands=commands, hero=hero)
        # print("une bombe sous vos pieds explose, vous mourrez")
        # hero.health = 0

    def upgrade_weapon(self):
        if self.hero.gold >= 25:
            if self.hero.force >= 70:
                print(page_dialog["stat_already_maxed"])
                return
            print(page_dialog["armure_lvl_up"])
            self.hero.force += 10
            self.hero.gold -= 25
        else:
            print(page_dialog["no_monnaie"])

    def upgrade_armor(self):
        if self.hero.gold >= 25:
            if self.hero.armor >= 70:
                print(page_dialog["stat_already_maxed"])
                return
            self.hero.armor += 10
            self.hero.gold -= 25
            print(page_dialog["arme_lvl_up"])
        else:
            print(page_dialog["no_monnaie"])
