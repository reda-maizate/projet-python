from characters.hero import Hero
from dungeon.dungeon import Dungeon, loop
from dungeon.exits import *
from game.game_settings import Dice


class Game:
    # Character hero
    # Shop shop
    # Home(Room) home
    def __init__(self):
        player_name = input("Quel est ton nom, jeune pucelle ?")
        self.hero = Hero(player_name)
        self.room = Home(self.hero)
        self.exit = False
        self.dungeon = loop()

    def launch(self):
        print("Qu'est-ce-qu'on fait maintenant chef")
        choices = ["%s : %s\n" % (door.name, door.value['index']) for door in Exits]
        indexes = [Exits[e].value["index"] for e in Exits.__members__.keys()]
        enums = [e.name for e in Exits]

        print(enums)
        while True:
            try:
                user_choice = int(input("".join(choices)))
                if user_choice in indexes:
                    break
                print("Jconnais pas '%d'" % user_choice)

            except ValueError:
                print("Pourquoi tu m'embrouilles")

        self.room = Exits[enums[user_choice - 1]].value["goto"](self.hero)

    def run(self):

        # self.room.display()  # todo add display to all Rooms (using commands)
        # OR
        # display(self.room.commands)  # you decide

        while not self.exit:
            self.launch()
            self.display()
            self.combat()
            self.isDead()

            if not self.hero:
                self.room = None
                continue

            cmd = input("{0} ~ P.V:{1}/{2} Att:{3} Dod:{4} Or:{05}>>> ".format(self.hero.name, self.hero.health,
                                                                               self.hero.maxHealth, self.hero.force,
                                                                               self.hero.dodge,
                                                                               self.hero.gold)).strip()

            if cmd.lower() == "quitter":
                self.exit = True
            elif cmd.lower() in self.room.exits:
                self.room = next(self.dungeon)
            elif cmd.lower() == "t" or cmd.lower() == "am":
                if self.room.monsters:
                    self.hero.fight(self.room.monsters[0])
                else:
                    print("Aucun monstre dans la salle mon reuf!")

    def combat(self):
        for monster in self.room.monsters:
            fightOrder = Dice(1).get_value()
            if fightOrder:
                self.hero.fight(monster)
                monster.fight(self.hero)

    def isDead(self):
        if self.hero.health <= 0:
            print("T'ES MOOOOOOOORTTT ! GAME OVER BATARD MTN VA TRAVAILLER!")
            self.hero = None
            return

        monstersRemaining = []
        for monster in self.room.monsters:
            if monster.health <= 0:
                print("Le monstre est mort !!!!!!!!!")
                self.hero.gold += monster.gold
            else:
                monster.append(monstersRemaining)
        self.room.monsters = monstersRemaining

    def display(self):
        print(self.room.name)
        print(self.room.description)
        if self.room.monsters:
            print("Monstre(s) présent(s): {0}".format(", ".join([d.name for d in self.room.monsters])))


