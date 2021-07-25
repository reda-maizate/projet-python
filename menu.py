import os


def menu():
    global choice
    print("---- BIENVENUE SUR DUNGEON CRAWLER ----")
    choices = [i for i in os.listdir("extraData/dialogs") if i != "empty_keys.json"]
    while True:
        try:
            print("0: Hard")
            print("1: Soft")
            user_choice = int(input("Quelle version souhaitez-vous jouer ?\n"))
            if user_choice < len(choices):
                if user_choice == 0:
                    choice = choices[0]
                elif user_choice == 1:
                    choice = choices[1]
                print(sep="\n\n")
                break
        except ValueError:
            print(f"Veuillez insérer une valeur entre 0 et {len(choices)}")

    return choice
