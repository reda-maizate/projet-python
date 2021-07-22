from game.game_settings import Dice
from characters.character import Character


class Hero(Character):
    def __init__(self, name):
        self.weapon = None
        self.pride = 0
        self.dodge = Dice(15).get_value()
        name = name
        gold = 0
        force = Dice(30).get_value()
        maxHealth = 100
        super().__init__(name, maxHealth, force, gold)

    def attack(self):
        if self.weapon:
            return self.force + self.weapon.force
        else:
            return self.force

    """
    def fight(self, monster):
        attackRoll = Dice().get_value()
        defenseRoll = Dice().get_value()

        #if dodgeRoll > 2:
        #    ...

        #if not self.weapon:
        if defenseRoll > attackRoll:
            print(f"Haaan tu viens de te manger une esquive tah Gogeta!!\n")

        elif attackRoll == defenseRoll:
            print(f"Coup égalité mgl, c'est une dinguerie on dirait un shonen\n")
            monster.health -= self.force / 2
            self.health -= monster.force / 2
        else:
            print(f"Ta mis une de ses bastos au {monster.name}, mashallah la puissance!\n")
            monster.health -= self.force
        #else:
        #    if defenseRoll > attackRoll:
        #        print(f"T'as sorti le glock il t'a esquiver comme les baqueux!\n")
        #    elif attackRoll == defenseRoll:
        #        print(f"Ta pas honte, tu sors le glock et vous avez tapé avec la même force, ai honte zebi!\n")
        #        monster.health -= self.force / 2
        #        self.health -= monster.force / 2
        #    else:
        #        print(f"Ta sorti la AK, {monster.name} a fait caca!\n")
        #        monster.health -= self.force
        """

    def sleep(self):
        self.health = self.maxHealth

    def isDead(self):
        if self.health <= 0:
            print("T'ES MOOOOOOOORTTT ! GAME OVER BATARD MTN VA TRAVAILLER!")
            return True
        return False
