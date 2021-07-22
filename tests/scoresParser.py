import random

if __name__ == "__main__":
    player_max_score = random.randint(0, 200)
    player_name = "newest player"

    with open("../extraData/scores.txt", "r+") as f:
        file_text = f.readlines()
        scores_names = dict(map(lambda line: (line.split(" -- ")[1].strip(), int(line.split(" -- ")[0])), file_text))

        scores_names[player_name] = player_max_score

        scores_names = dict(sorted(scores_names.items(), key=lambda item: item[1], reverse=True))

        f.seek(0)
        f.truncate()

        for index, player in enumerate(scores_names):
            if index < 3:
                f.write(" ".join([ str(scores_names[player]), "--",player, "\n"]))
