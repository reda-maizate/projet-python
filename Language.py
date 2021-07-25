import json
import os

dialogs = {}


def loadDialogs(filename):
    global dialogs
    with open(f"extraData/dialogs/{filename}", "r", encoding="utf-8") as f:
        dialogs = json.load(f)


default_file = "fr_FR.json"
loadDialogs(default_file)
