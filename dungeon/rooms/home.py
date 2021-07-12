from characters.hero import Hero
from dungeon.rooms.room import Room


class Home(Room):
    def __init__(self, hero: Hero):
        from dungeon.exits import Exits

        # Exits = list(Exits)
        self.hero = hero
        commands = {
            "dormir": hero.sleep
        }
        print(Exits.NEXT_ROOM.value["index"])
        exits = [Exits.SHOP, Exits.NEXT_ROOM]
        super().__init__("Maison", "Assieds-toi mon reuf, prends un verre", exits=exits,
                         commands=commands)

    # def __str__(self):
    #     return super.__str__(self)
