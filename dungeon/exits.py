from enum import Enum

class Exits(Enum):
    HOME = {
        "text": utils.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["home"],
        "index": 1
    }
    SHOP = {
        "text": utils.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["shop"],
        "index": 2
    }
    NEXT_ROOM = {
        "text": utils.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["next_room"],
        "index": 3
    }
