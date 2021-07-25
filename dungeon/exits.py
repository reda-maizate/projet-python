from enum import Enum


class Exits(Enum):
    HOME = {
        "text": "Retour au tieks",
        "index": 1
    }
    SHOP = {
        "text": "Go faire les boutiques",
        "index": 2
    }
    NEXT_ROOM = {
        "text": "Plus loiiiiiiin dans le donjon",
        "index": 3
    }
