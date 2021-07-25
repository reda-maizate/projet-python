import json

dialogs = {}


def loadDialogs(filename):
    global dialogs
    with open(f"extraData/dialogs/{filename}", "r", encoding="utf-8") as f:
        dialogs = json.load(f)

