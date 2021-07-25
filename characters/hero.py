from game.Dice import Dice
from characters.character import Character
import utils
import Language

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
        super().__init__(name, maxHealth, force, gold , armor)

    def sleep(self):
        print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["hero"]["sleep"])
        self.health = self.maxHealth

    def isDead(self):
        if self.health <= 0:
            print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["hero"]["death"])
            return True
        return False

    def __str__(self):
        return "{0} ~ P.V:{1}/{2} Att:{3} Arm:{4} Or:{05}>>> ".format(
            self.name, self.health,
            self.maxHealth, self.force,
            self.armor,
            self.gold)
