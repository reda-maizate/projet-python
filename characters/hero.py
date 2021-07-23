from game.game_settings import Dice
from characters.character import Character


class Hero(Character):
    def __init__(self, name):
        self.score = 0
        self.weapon = None
        self.pride = 0
        self.armor = 0
        gold = 60000
        force = Dice(30).get_value()
        maxHealth = 100
        super().__init__(name, maxHealth, force, gold)

    def attack(self):
        if self.weapon:
            return self.force + self.weapon.force
        else:
            return self.force

    def sleep(self):
        print("Un bon gros dodo wallah")
        self.health = self.maxHealth

    def isDead(self):
        if self.health <= 0:
            print("T'ES MOOOOOOOORTTT ! GAME OVER BATARD MTN VA TRAVAILLER!")
            return True
        return False

    def __str__(self):
        return "{0} ~ P.V:{1}/{2} Att:{3} Arm:{4} Or:{05}>>> ".format(
            self.name, self.health,
            self.maxHealth, self.force,
            self.armor,
            self.gold)
