from game.Dice import Dice


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
            print("Haaan %s vient de se manger une esquive tah Gogeta par %s!!\n" % (self.name, other.name))
            print("%s ne prend pas de dégats" % other.name)

        elif attackRoll == defenseRoll:
            print("%s et %s sont surpuissants on peut pas les départager,\n"
                  "Coup égalité mgl, c'est une dinguerie on dirait un shonen\n" % (self.name , other.name))
            otherDammages = max(0, (self.force / 2) - (other.armor / 10))
            selfDammages = max(0, (other.force / 2) - (self.armor / 10))
            other.health -= otherDammages
            self.health -= selfDammages
            displayLifePointsLost(self.name, selfDammages)
            displayLifePointsLost(other.name, otherDammages)
        else:
            print("%s met une de ces bastos à %s, mashallah la puissance!\n" % (self.name, other.name))
            otherDammages = max(0, self.force - (other.armor / 10))
            other.health -= otherDammages
            displayLifePointsLost(other.name, otherDammages)


def displayLifePointsLost(characterHealth, pointsLost):
    print("%s perd %d points de vie" % (characterHealth, pointsLost))
