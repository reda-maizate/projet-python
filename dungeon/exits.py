from enum import Enum
import Language


class Exits(Enum):
    HOME = {
        "text": Language.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["home"],
        "index": 1
    }
    SHOP = {
        "text": Language.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["shop"],
        "index": 2
    }
    NEXT_ROOM = {
        "text": Language.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]["next_room"],
        "index": 3
    }
