import Language
import utils
from characters.hero import Hero
from dungeon.rooms.home import Home


class Game:
    def __init__(self):
        player_name = input(Language.dialogs["dungeon_crawler"]["classes"]["game"]["init"]["prompt"])
        self.hero = Hero(player_name)
        self.room = Home(self.hero)
        self.exit = False

    def next_room(self):
        print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["welcome"])
        question = Language.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["ask"]
        self.exit = input(question) not in ["y", ""]

        if not self.exit:
            choices = self.room.choices()
            while True:
                try:
                    user_choice = int(input("".join(choices)))
                    if user_choice < len(self.room.exits):
                        break
                    print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["incorrect_number"] % user_choice)

                except ValueError:
                    print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["incorrect_answer"])

            self.room = utils.whichRoom(self, user_choice)

    def run(self):
        while not self.exit:
            print(self.room)
            self.room.use()
            if self.hero.isDead():
                break
            self.next_room()

        utils.scoreManager(self.hero)
        print(Language.dialogs["dungeon_crawler"]["classes"]["game"]["run"]["end_game"] % self.hero.score)
        utils.displayBestPlayers()
