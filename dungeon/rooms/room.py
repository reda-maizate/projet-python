import Language

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["room"]


class Room:
    def __init__(self, name="Room Name", description="Room Desc", commands=None, exits=None, monsters=None, hero=None):
        if commands is None:
            commands = {}
        if monsters is None:
            monsters = []
        if exits is None:
            exits = []
        if hero is None:
            print(page_dialog["hero_nonexistant"])
            exit(1)

        self.name = name
        self.description = description
        self.exits = exits
        self.monsters = monsters
        self.commands = commands
        self.hero = hero

    def __str__(self):
        return page_dialog["to_string"] + self.name + " \n" + self.description + " "

    def choices(self):
        return ["%s : %s\n" % (index, door.value['text']) for index, door in enumerate(self.exits)]

    def use(self):

        interact_with_room = True
        while interact_with_room:
            print(page_dialog["commands"])
            for cmd in self.commands:
                print("\t-", cmd)
            print("\t-", page_dialog["out"])

            cmd = input(self.hero).strip().lower()

            if cmd in self.commands:
                self.commands[cmd]()

            if cmd == page_dialog["out"]:
                interact_with_room = False
