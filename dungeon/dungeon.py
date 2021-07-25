import random
from time import sleep

from characters.hero import Hero
from characters.monster import Monster
from dungeon.exits import Exits
from game.Dice import Dice
from dungeon.rooms.room import *

import utils


def init_power():
    def power_(func):
        func.used = 0
        return func

    return power_


@init_power()
def use_power():
    use_power.used += 1
    if use_power.used > 1:
        print("Tu peux pas faire ça poto")
    else:
        print("la puissaaaaance")


class Dungeon(Room):
    def __init__(self, hero: Hero):
        exitDescription = ""
        commands = {"superPower": use_power()}  # todo generate commands

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
            print(utils.dialogs["dungeon_crawler"]["classes"]["game"]["display"]["room_content"] % (
                monsters_quantity,
                ", ".join([d.name for d in self.monsters])
            ))
            if rounds == 1:
                text = "\nLe combat commence"
            else:
                text = "\nLe combat continue"

            print(text)
            print("Actions disponibles:")
            for cmd in self.commands:
                print("\t-", cmd)
            print("\t- attaquer")
            print("\t- defendre")

            attack_or_defense = input(self.hero)

            tmp_force = self.hero.force
            tmp_def = self.hero.armor

            humansFights = attack_or_defense == "attaquer"
            if not humansFights:
                self.hero.force, self.hero.armor = 0, 80

            self.combat(humansFights=humansFights)

            self.hero.force = tmp_force
            self.hero.armor = tmp_def

            print()

        print("Aucun monstre dans la salle mon reuf!")
        print("Ca sert à rien de taper dans le vide y'a pas de Jnoûn")

    def combat(self, humansFights=True):
        monstersRemaining = []
        for monster in self.monsters:
            fightOrder = Dice(1).get_value()
            if fightOrder:
                if humansFights:
                    self.hero.fight(monster)
                monster.fight(self.hero)
            else:
                monster.fight(self.hero)
                if humansFights:
                    self.hero.fight(monster)

            if monster.health <= 0:
                self.hero.gold += monster.gold
                self.hero.score += monster.maxHealth
                print("Le monstre est mort !!!!!!!!!")
            elif self.hero.health <= 0:
                break
            else:
                monstersRemaining.append(monster)
            sleep(2)
        self.monsters = monstersRemaining

    def fillMonsters(self):
        numMonster = Dice(3).get_value()
        for _ in range(numMonster):
            self.monsters.append(Monster())
