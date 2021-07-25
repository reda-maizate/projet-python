import os

from characters.hero import Hero
from dungeon.dungeon import Dungeon
from dungeon.exits import Exits
from dungeon.rooms.home import Home
from dungeon.rooms.shop import Shop


def whichRoom(game, user_choice):
    enumRoom = game.room.exits[user_choice]

    if enumRoom == Exits.NEXT_ROOM:
        return Dungeon(hero=game.hero)
    elif enumRoom == Exits.HOME:
        return Home(hero=game.hero)
    elif enumRoom == Exits.SHOP:
        return Shop(hero=game.hero)


def scoreManager(hero: Hero):
    with open("extraData/scores.txt", "r+", encoding="utf-8") as f:
        file_text = f.readlines()
        scores_names = dict(map(lambda line: (line.split(" -- ")[1].strip(), int(line.split(" -- ")[0])), file_text))

        scores_names[hero.name] = hero.score

        scores_names = dict(sorted(scores_names.items(), key=lambda item: item[1], reverse=True))

        f.seek(0)
        f.truncate()

        for index, player in enumerate(scores_names):
            if index < 3:
                f.write(" ".join([str(scores_names[player]), "--", player, "\n"]))


def displayBestPlayers():
    with open("extraData/scores.txt", "r+", encoding="utf-8") as f:
        best = f.readlines()
        print("\n".join(best))
