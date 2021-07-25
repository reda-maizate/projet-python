from characters.hero import Hero
from dungeon.rooms.room import Room

from dungeon.exits import Exits
import Language

page_dialog = Language.dialogs["dungeon_crawler"]["classes"]["home"]


class Home(Room):
    def __init__(self, hero: Hero):
        commands = {
            page_dialog["commands"][0]: hero.sleep
        }
        # print(Exits.NEXT_ROOM.value["index"])
        exits = [Exits.SHOP, Exits.NEXT_ROOM]
        super().__init__(page_dialog["default_name"], page_dialog["default_desc"], exits=exits,
                         commands=commands , hero=hero)

    # def __str__(self):
    #     return super.__str__(self)
