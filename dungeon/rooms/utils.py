from dungeon.dungeon import Dungeon
from dungeon.exits import Exits
from dungeon.rooms.home import Home
from dungeon.rooms.shop import Shop


def whichRoom(game, user_choice):
    enumRoom = game.room.exits[user_choice]

    if enumRoom == Exits.NEXT_ROOM:
        return Dungeon(game.hero)
    elif enumRoom == Exits.HOME:
        return Home(game.hero)
    elif enumRoom == Exits.SHOP:
        return Shop(game.hero)
    else:
        return None
