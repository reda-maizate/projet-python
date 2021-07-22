class Room:
    def __init__(self, name="Room Name", description="Room Desc", commands=None, exits=None, monsters=None):
        if commands is None:
            commands = {}
        if monsters is None:
            monsters = []
        if exits is None:
            exits = []

        self.name = name
        self.description = description
        self.exits = exits
        self.monsters = monsters
        self.commands = commands

    def __str__(self):
        return self.__class__.__name__ + "\n" + self.name + " \n" + self.description + " "

    def choices(self):
        return ["%s : %s\n" % (index, door.name) for index, door in enumerate(self.exits)]

    def use(self):
        print(self.commands)
        print("Il n'y a rien à faire ici en fait")

    def next(self):
        pass
