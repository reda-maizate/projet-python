from game.game_settings import Dice


class Character:
    def __init__(self, name, maxHealth, force, gold, armor = 0):
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
                  "Coup égalité mgl, c'est une dinguerie on dirait un shonen\n")
            otherDammages = (self.force / 2) - (other.armor / 2)
            selfDammages = (other.force / 2) - (self.armor / 2)
            other.health -= otherDammages
            self.health -= selfDammages
            print("%s perd %d points de vie" % (self.name , selfDammages) )
            print("%s perd %d points de vie" % (other.name , otherDammages) )

        else:
            print("%s met une de ces bastos à %s, mashallah la puissance!\n" % (self.name ,other.name))
            other.health -= self.force * (other.armor/100)
