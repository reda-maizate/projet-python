from characters.hero import Hero
from dungeon.rooms.home import Home
from game.game_settings import Dice
from dungeon.rooms.utils import whichRoom


class Game:
    def __init__(self):
        player_name = input("Quel est ton nom, jeune pucelle ?")
        self.hero = Hero(player_name)
        self.room = Home(self.hero)
        self.exit = False

    def next_room(self):
        print("Qu'est-ce-qu'on fait maintenant chef")
        question = "Tu veux continuer ton périple ? [y]/n"
        self.exit = input(question) not in ["y", ""]

        if not self.exit:
            choices = self.room.choices()
            while True:
                try:
                    user_choice = int(input("".join(choices)))
                    if user_choice < len(self.room.exits):
                        break
                    print("Jconnais pas l'option '%d'" % user_choice)

                except ValueError:
                    print("Pourquoi tu m'embrouilles")

            self.room = whichRoom(self, user_choice)

    def run(self):
        while not self.hero.isDead() and not self.exit:
            print(self.room)
            self.room.use()
            self.next_room()

            #
            # if cmd.lower() == "quitter":
            #     self.exit = True
            #
            #
            # # print(self.room.exits.)
            # elif cmd.lower() in self.room.exits:  # todo use values of enums
            #     self.room = Home(
            #         self.hero) if cmd.lower() == Exits.HOME else Dungeon(
            #         self.hero) if cmd.lower() == Exits.NEXT_ROOM else Shop(self.hero)
            #
            # elif cmd.lower() == "t" or cmd.lower() == "am":
            #     if self.room.monsters:
            #         self.hero.fight(self.room.monsters[0])
            #     else:
            #         print("Aucun monstre dans la salle mon reuf!")
            # elif cmd.lower() == 'leave':
            #     break
        print("end Game , score : ", 809230, "pts")

    def combat(self):
        for monster in self.room.monsters:
            fightOrder = Dice(1).get_value()
            if fightOrder:
                self.hero.fight(monster)
                monster.fight(self.hero)

        #todo jsp quoi faire de ça

        # monstersRemaining = []
        # for monster in self.room.monsters:
        #     if monster.health <= 0:
        #         print("Le monstre est mort !!!!!!!!!")
        #         self.hero.gold += monster.gold
        #     else:
        #         monster.append(monstersRemaining)
        # self.room.monsters = monstersRemaining


    #todo this should belong to room OR dungeon
    def display(self):
        print(self.room.name)
        print(self.room.description)

        for index, cmd in enumerate(self.room.commands):
            print(index, cmd, sep=" : ")

        if self.room.monsters:
            print("Monstre(s) présent(s): {0}".format(", ".join([d.name for d in self.room.monsters])))
