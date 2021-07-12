from game.game_settings import Dice
from characters.monster import Monster


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.maxHealth = 100
        self.attackRoll = 3 * Dice().value
        self.defense = 5 * Dice().value
        self.weapon = None
        self.gold = 0
        self.pride = 0

    def attack(self):
        if self.weapon:
            return self.attackRoll + self.weapon.power
        else:
            return self.attackRoll

    def fight(self, monster):
        attack = self.attackRoll
        defense = Monster.defense

        if not self.weapon:
            if defense > attack:
                print(f"Haaan tu viens de te manger une esquive tah Gogeta!!\n")

            elif attack == defense:
                print(f"Coup égalité mgl, c'est une dinguerie on dirait un shonen\n")
            else:
                print(f"Ta mis une de ses bastos au {monster.name}, mashallah la puissance!\n")
        else:
            if defense > attack:
                print(f"T'as sorti le glock il t'a esquiver comme les baqueux!\n")
            elif attack == defense:
                print(f"Ta pas honte, tu sors le glock et vous avez tapé avec la même force, ai honte zebi!\n")
            else:
                print(f"Ta tirer sur {monster.name}, il t'as même pas dit choucrane\n")
