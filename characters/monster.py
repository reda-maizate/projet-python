from game.Dice import Dice
from characters.character import Character
import Language

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["monster"]

class Monster(Character):
    def __init__(self):
        self.force = Dice(25).get_value() + 10
        self.dodge = Dice(15).get_value()
        health = Dice(70).get_value()
        self.health = health
        self.maxHealth = health

        if health > 40:
            self.name = page_dialog["big"]
            self.gold = Dice(10).get_value() + 20
            self.force = Dice(25).get_value()
        elif 40 > health > 25:
            self.name = page_dialog["classic"]
            self.gold = Dice(10).get_value() + 10
            self.force = Dice(25).get_value()
        else:
            self.name = page_dialog["small"]
            self.gold = Dice(10).get_value()
            self.force = Dice(25).get_value()

        super().__init__(self.name, self.maxHealth, self.force, self.gold)


