from game.game_settings import Dice


class Character:
    def __init__(self, name, maxHealth, force, gold):
        self.name = name
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.force = force
        self.gold = gold

    def fight(self, other):
        attackRoll = Dice().get_value()
        defenseRoll = Dice().get_value()

        if defenseRoll > attackRoll:
            print(f"Haaan tu viens de te manger une esquive tah Gogeta!!\n")

        elif attackRoll == defenseRoll:
            print(f"Coup égalité mgl, c'est une dinguerie on dirait un shonen\n")
            other.health -= self.force / 2
            self.health -= other.force / 2
        else:
            print(f"Ta mis une de ses bastos au {other.name}, mashallah la puissance!\n")
            other.health -= self.force
