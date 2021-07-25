import Language
from characters.character import Character
from game.Dice import Dice

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["game"]["hero"]


class Hero(Character):
    def __init__(self, name):
        self.score = 0
        self.weapon = None
        self.pride = 0
        gold = 0
        force = 10 + Dice(30).get_value()
        maxHealth = 100
        self.health = maxHealth
        armor = 15
        super().__init__(name, maxHealth, force, gold, armor)

    def sleep(self):
        print(page_dialog["sleep"])
        self.health = self.maxHealth

    def isDead(self):
        if self.health <= 0:
            print(page_dialog["death"])
            self.score -= 30
            return True
        return False

    def __str__(self):
        return "{0} ~ P.V:{1}/{2} Att:{3} Arm:{4} Or:{05}>>> ".format(
            self.name, self.health,
            self.maxHealth, self.force,
            self.armor,
            self.gold)
