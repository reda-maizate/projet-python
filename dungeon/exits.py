from enum import Enum
import Language

page_dialogs = Language.dialogs["dungeon_crawler"]["classes"]["game"]["exit"]


class Exits(Enum):
    HOME = {
        "text": page_dialogs["home"],
        "index": 1
    }
    SHOP = {
        "text": page_dialogs["shop"],
        "index": 2
    }
    NEXT_ROOM = {
        "text": page_dialogs["next_room"],
        "index": 3
    }
