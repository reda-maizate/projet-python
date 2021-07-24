import random

from characters.hero import Hero
from characters.monster import Monster
from dungeon.exits import Exits
from game.game_settings import Dice
from dungeon.rooms.room import *


def nothing():
    print("test")


class Dungeon(Room):
    def __init__(self, hero: Hero):
        exitDescription = ""
        commands = {"what": nothing}  # todo generate commands

        exits = [Exits.NEXT_ROOM]
        can_tp_home = random.random() <= 1 / 5
        if can_tp_home:
            exits.append(Exits.HOME)
            exitDescription = "\nJvois une porte vers la maison au fond là bas"

        super().__init__("Bas des blocs", "Antre sombre et menaçante" + exitDescription, commands, exits, [], hero)
        self.fillMonsters()

    def use(self):
        rounds = 0
        while self.monsters:
            rounds += 1
            monsters_quantity = len(self.monsters)
            print("%d Monstre(s) présent(s): %s" % (
                monsters_quantity,
                ", ".join([d.name for d in self.monsters])
            ))
            if rounds == 1:
                text = "\nLe combat commence"
            else:
                text = "\nLe combat continue"

            print(text , "tu préfères : \n\t-attaquer\n\t-defendre")
            attack_or_defense = input(self.hero)

            tmp_force = self.hero.force
            tmp_def = self.hero.armor

            if attack_or_defense == "defense":
                self.hero.force = 0
                self.hero.armor = 80
            self.combat()

            self.hero.force = tmp_force
            self.hero.armor = tmp_def

            print()


        print("Aucun monstre dans la salle mon reuf!")
        print("Ca sert à rien de taper dans le vide y'a pas de Jnoûn")

    def combat(self):
        monstersRemaining = []
        for monster in self.monsters:
            fightOrder = Dice(1).get_value()
            if fightOrder:
                self.hero.fight(monster)
                monster.fight(self.hero)
            else:
                monster.fight(self.hero)
                self.hero.fight(monster)
            if monster.health <= 0:
                self.hero.gold += monster.gold
                print("Le monstre est mort !!!!!!!!!")
            else:
                monstersRemaining.append(monster)

        self.monsters = monstersRemaining

    def fillMonsters(self):
        numMonster = Dice(3).get_value()
        for _ in range(numMonster):
            self.monsters.append(Monster())
