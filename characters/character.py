from game.Dice import Dice
import Language

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["game"]["character"]

class Character:

    def __init__(self, name, maxHealth, force, gold, armor=0):
        self.name = name
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.force = force
        self.gold = gold
        self.armor = armor

    def fight(self, other):
        attackRoll = Dice().get_value()
        defenseRoll = Dice().get_value()

        if defenseRoll > attackRoll:
            print(page_dialog["defense_sup_attaque"] % (self.name, other.name, other.name))

        elif attackRoll == defenseRoll:
            print(page_dialog["defense_equal_attaque"] % (self.name, other.name))
            otherDammages = max(0, (self.force / 2) - (other.armor / 10))
            selfDammages = max(0, (other.force / 2) - (self.armor / 10))
            other.health -= otherDammages
            self.health -= selfDammages
            displayLifePointsLost(self.name, selfDammages)
            displayLifePointsLost(other.name, otherDammages)
        else:
            print(page_dialog["defense_inf_attaque"] % (self.name, other.name))
            otherDammages = max(0, self.force - (other.armor / 10))
            other.health -= otherDammages
            displayLifePointsLost(other.name, otherDammages)


def displayLifePointsLost(characterHealth, pointsLost):
    print(page_dialog["lose_hp"] % (characterHealth, pointsLost), end="\n\n")
