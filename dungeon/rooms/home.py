from characters.hero import Hero
from dungeon.rooms.room import Room

from dungeon.exits import Exits


class Home(Room):
    def __init__(self, hero: Hero):
        commands = {
            "dormir": hero.sleep
        }
        # print(Exits.NEXT_ROOM.value["index"])
        exits = [Exits.SHOP, Exits.NEXT_ROOM]
        super().__init__("Maison", "Assieds-toi mon reuf, prends un verre", exits=exits,
                         commands=commands , hero=hero)

    # def __str__(self):
    #     return super.__str__(self)
