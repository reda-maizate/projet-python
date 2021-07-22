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
        return self.__class__.__name__ + "\n" + self.name + " \n" + self.description + " "

    def choices(self):
        return ["%s : %s\n" % (index, door.name) for index, door in enumerate(self.exits)]

    def use(self):

        print("Actions disponibles")
        for cmd in self.commands:
            print("\t-", cmd)

        cmd = input("{0} ~ P.V:{1}/{2} Att:{3} Dod:{4} Or:{05}>>> ".format(self.hero.name, self.hero.health,
                                                                           self.hero.maxHealth, self.hero.force,
                                                                           self.hero.dodge,
                                                                           self.hero.gold)).strip()

        if cmd in self.commands:
            self.commands[cmd]()

    def next(self):
        pass
