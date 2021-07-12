from enum import Enum

from dungeon.rooms.home import Home
from dungeon.rooms.shop import Shop


class Exits(Enum):
    HOME = {
        "index": 1,
        "goto": Home,
    }
    SHOP = {
        "index": 2,
        "goto": Shop,
    }
    NEXT_ROOM = {
        "index": 1,
        "goto": Home,
    }
