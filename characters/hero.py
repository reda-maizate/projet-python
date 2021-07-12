from game.game_settings import Dice
from characters.character import Character


class Hero(Character):
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.gold = 0
        self.pride = 0
        self.force = Dice(30).get_value()
        self.dodge = Dice(15).get_value()
        self.health = 100
        self.maxHealth = 100
        super().__init__(self.name, self.maxHealth, self.force, self.gold)

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
