import random
from time import sleep

import Language
from characters.hero import Hero
from characters.monster import Monster
from dungeon.exits import Exits
from dungeon.rooms.room import *
from game.Dice import Dice

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["game"]


def init_power():
    def power_(func):
        func.used = 0
        return func

    return power_


@init_power()
def use_power():
    use_power.used += 1
    # if use_power.used > 1:
    #     print(page_dialog["power"]["cannot_use_power"])
    # else:
    #     print(page_dialog["power"]["use_power"])


class Dungeon(Room):
    def __init__(self, hero: Hero):
        exitDescription = ""
        commands = {"superPower": use_power()}

        exits = [Exits.NEXT_ROOM]
        can_tp_home = random.random() <= 1 / 5
        if can_tp_home:
            exits.append(Exits.HOME)
            exitDescription = page_dialog["dungeon"]["sortie"]
        exitDescription = page_dialog["dungeon"]["description"] + exitDescription
        room_name = page_dialog["next_room"]["name"]
        super().__init__(room_name, exitDescription, commands, exits, [], hero)
        self.fillMonsters()

    def use(self):
        rounds = 0
        while self.monsters:
            rounds += 1
            monsters_quantity = len(self.monsters)
            print(page_dialog["display"]["room_content"] % (
                monsters_quantity,
                ", ".join([d.name + "(%d/%d)" % (d.health, d.maxHealth) for d in self.monsters])
            ))
            if rounds == 1:
                text = page_dialog["round"]["start"]
            else:
                text = page_dialog["round"]["continue"]

            print("\n" + text)
            print(page_dialog["round"]["ask_action"])
            for cmd in self.commands:
                print("\t-", cmd)
            print("\t- " + page_dialog["round"]["attaquer"])
            print("\t- " + page_dialog["round"]["defendre"])

            attack_or_defense = input(self.hero)
            print()
            tmp_force = self.hero.force
            tmp_def = self.hero.armor

            humansFights = attack_or_defense == "attaquer"
            if not humansFights:
                self.hero.force, self.hero.armor = 0, 80

            self.combat(humansFights=humansFights)

            self.hero.force = tmp_force
            self.hero.armor = tmp_def

            print()

        print(page_dialog["next_room"]["no_monster"])

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
                print(page_dialog["combat"]["monster_dead"])
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
