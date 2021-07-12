from game.game_settings import Dice
from characters.character import Character


class Monster(Character):
    def __init__(self):
        self.force = Dice(25).get_value() + 10
        self.dodge = Dice(15).get_value()
        health = Dice(70).get_value()
        self.health = health
        self.maxHealth = health

        if health > 40:
            self.name = "Grand Monstre"
            self.gold = Dice(10).get_value() + 20
            self.force = Dice(25).get_value()
        elif 40 > health > 25:
            self.name = "Monstre"
            self.gold = Dice(10).get_value() + 10
            self.force = Dice(25).get_value()
        else:
            self.name = "Petit Monstre"
            self.gold = Dice(10).get_value()
            self.force = Dice(25).get_value()

        super().__init__(self.name, self.maxHealth, self.force, self.gold)

    """
    def fight(self, hero):
        attackRoll = Dice().get_value()
        defenseRoll = Dice().get_value()

        if defenseRoll > attackRoll:
            print(f"Haaan tu viens de te manger une esquive tah Gogeta!!\n")

        elif attackRoll == defenseRoll:
            print(f"Coup égalité mgl, c'est une dinguerie on dirait un shonen\n")
            hero.health -= self.force / 2
            self.health -= hero.force / 2
        else:
            print(f"Ta mis une de ses bastos au {hero.name}, mashallah la puissance!\n")
            hero.health -= self.force
    """
