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
        return self.name + " " + self.description
