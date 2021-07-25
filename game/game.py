import utils


class Game:
    def __init__(self):
        player_name = input(utils.dialogs["dungeon_crawler"]["classes"]["game"]["init"]["prompt"])
        self.hero = Hero(player_name)
        self.room = Home(self.hero)
        self.exit = False

    def next_room(self):
        print(utils.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["welcome"])
        question = utils.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["ask"]
        self.exit = input(question) not in ["y", ""]

        if not self.exit:
            choices = self.room.choices()
            while True:
                try:
                    user_choice = int(input("".join(choices)))
                    if user_choice < len(self.room.exits):
                        break
                    print(utils.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["incorrect_number"] % user_choice)

                except ValueError:
                    print(utils.dialogs["dungeon_crawler"]["classes"]["game"]["next_room"]["incorrect_answer"])

            self.room = whichRoom(self, user_choice)

    def run(self):
        while not self.exit:
            print(self.room)
            self.room.use()
            if self.hero.isDead():
                break
            self.next_room()

        scoreManager(self.hero)
        print(utils.dialogs["dungeon_crawler"]["classes"]["game"]["run"]["end_game"] % self.hero.score)
        displayBestPlayers()
