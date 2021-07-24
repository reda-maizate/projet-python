class Room:
    def __init__(self, name="Room Name", description="Room Desc", commands=None, exits=None, monsters=None, hero=None):
        if commands is None:
            commands = {}
        if monsters is None:
            monsters = []
        if exits is None:
            exits = []
        if hero is None:
            print("Vous devez exister pour rentrer dans cette salle")
            exit(1)

        self.name = name
        self.description = description
        self.exits = exits
        self.monsters = monsters
        self.commands = commands
        self.hero = hero

    def __str__(self):
        return "Ta position : " + self.name + " \n" + self.description + " "

    def choices(self):
        return ["%s : %s\n" % (index, door.value['text']) for index, door in enumerate(self.exits)]

    def use(self):

        interact_with_room = True
        while interact_with_room:
            print("Actions disponibles:")
            for cmd in self.commands:
                print("\t-", cmd)
            print("\t-", "sortir")

            cmd = input(self.hero).strip().lower()

            if cmd in self.commands:
                self.commands[cmd]()

            if cmd == "sortir":
                interact_with_room = False
