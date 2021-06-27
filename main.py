import random


class Dice(int):
    """
    This is a fancy Dice object.
    eg. Dice(numberOfSides)

    Has multiplication override for rolling multiple Dice. It will roll the same type of die the number of times specified.
    eg. 3*Dice(6)
    eg. Dice(6)*3

    Has highest and lowest methods for getting the highest or lower number of Dice from a given roll.
    Best 2 out of 3 eg. 3*Dice(6).highest(2)
    Worst 2 out of 3 eg. 3*Dice(6).lowest(2)
    """

    def __new__(self, sides=100):
        self.sides = sides
        self.value = self.getValue(self)
        self.values = []
        return super(self, self).__new__(self, self.value)

    def getValue(self):
        x = random.randrange(self.sides) + 1
        return x

    # It Looks and Acts like an Int
    #     repr and inheritance
    def __repr__(self):
        return str(self.value)

    def __mul__(self, other):
        self.values = []
        for die in range(other):
            self.values.append(self.getValue())
        self.value = sum(self.values)
        return self

    __rmul__ = __mul__

    def highest(self, num):
        """
        Get the highest Dice rolls out of a roll with multiple Dice.
        Best 2 out of 3 eg. 3*Dice(6).highest(2)
        """
        self.values.sort()
        self.value = sum(self.values[-num:])
        return self

    def lowest(self, num):
        """
        Get the lowest Dice rolls out of a roll with multiple Dice.
        Worst 2 out of 3 eg. 3*Dice(6).lowest(2)
        """
        self.values.sort()
        self.value = sum(self.values[:num])
        return self


class Character(object):
    """
    Player Character object
    Creates with randomized default values for att and def. Health starts at 100; Score and gold, 0.
    """

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.maxHealth = 100
        self.attackRoll = 3 * Dice(6)
        defenseRoll = 3 * Dice(6)
        self.defense = defenseRoll.highest(2).value
        self.weapon = None
        self.gold = 0
        self.score = 0

    # Using a Property to make this dynamic
    #    use with self.attack
    #    returns int value, attack+weapon modifier
    @property
    def attack(self):
        if self.weapon:
            return self.attackRoll.highest(2).value + self.weapon.power
        else:
            return self.attackRoll.highest(2).value

    def fight(self, daemon):
        """
        Method for fighting Daemons.
        Method takes a Daemon, returns nothing.
        """
        attack = Dice(self.attack)
        defense = Dice(daemon.defense)
        daemon.aggression = 10

        if not self.weapon:
            if defense > attack:
                print("Le {0} esquive lorsque vous vous élancez vers l'avant après un puissant coup de poing.".format(
                    daemon.name.lower()))
                print("\n")

            elif attack == defense:
                print("Le {0} bloque votre coup de poing avec ses serres mais vous voyez ses bras se tordre.".format(
                    daemon.name.lower()))
                print("\n")
                daemon.health -= attack / 2

            elif attack > defense:
                print(
                    "Vous entendez un bruit sourd et écoeurant lorsque votre coup de poing frappe la tête du {0}.".format(
                        daemon.name.lower()))
                print("\n")
                daemon.health -= attack

        else:
            if defense > attack:
                print("Le {0} esquive alors que vous vous élancez en avant avec un puissant {1} de votre {2}.".format(
                    daemon.name.lower(), self.weapon.attType, self.weapon.name.lower()))
                print("\n")

            elif attack == defense:
                print(
                    "Le {0} bloque votre {1} avec ses serres mais vous voyez ses bras se tordre sous l'effet de votre {2}.".format(
                        daemon.name.lower(), self.weapon.attType, self.weapon.name.lower()))
                print("\n")
                daemon.health -= attack / 2

            elif attack > defense:
                print(
                    "Vous entendez un bruit sourd et écœurant quand votre {1} touche la tête du {0} et que votre {2} s'enfonce un peu dans la peau écailleuse du {0}.".format(
                        daemon.name.lower(), self.weapon.attType, self.weapon.name.lower()))
                print("\n")
                daemon.health -= attack


class Daemon(object):
    """
    The Daemon object rolls for health, attack,defense, and gold then names the Daemon accordingly. The init function takes no input.
    """

    def __init__(self):
        healthRoll = 6 * Dice(10)
        healthValue = healthRoll.highest(5).value
        self.health = healthValue
        self.maxHealth = healthValue

        if healthValue > 40:
            self.name = "Grand Monstre"
            self.description = "Un Grand Monstre vous grogne dessus avec ses dents en forme de poignard alors qu'il empiète lentement sur votre espace. Sa forme sombre est difficile à voir, mais sa peau écailleuse brille dans la faible lumière des grottes."
            self.aggression = 10

        elif healthValue > 25:
            self.name = "Monstre"
            self.description = "Un Monstre te regarde prudemment alors que tu te promènes dans les grottes. Il garde un peu de distance, mais il commence à vous suivre pendant un moment. À chaque pas, vous pouvez entendre ses serres gratter le sol de la caverne."
            self.aggression = 5

        else:
            self.name = "Petit Monstre"
            self.description = "Un Petit Monstre se cache dans un recoin du mur de la caverne. Il semble se cacher de vous, mais chaque mouvement subtil fait danser la faible lumière de la grotte sur ses écailles brillantes."
            self.aggression = 1

        attackRoll = 3 * Dice(6)
        self.attack = attackRoll.highest(2).value
        defenseRoll = 3 * Dice(6)
        self.defense = defenseRoll.highest(2).value

        self.gold = int(Dice(6)) - 1

    def fight(self, player):
        """
        Daemon.fight takes a player character as input and returns nothing.
        """
        attack = Dice(self.attack)
        defense = Dice(player.defense)

        if defense > attack:
            print("Vous esquivez gracieusement lorsque le {0} vous frappe.".format(self.name.lower()))

        elif attack == defense:
            print("Vous essayez d'esquiver mais vous subissez quand même la force des coups portés par les {0}.".format(
                self.name.lower()))
            player.health -= attack / 2

        elif attack > defense:
            print("Le {0} ne vous dit pas salam et vous balaie avec ses serres et vous déchire.".format(self.name.lower()))
            player.health -= attack


class Weapon(object):
    """
    Simple Weapon type object template

    Takes default values as inputs
    """

    def __init__(self, name, attType, power):
        self.name = name
        self.attType = attType
        self.power = power


class Room(object):
    """
    Simple Weapon type object template

    Takes no inputs, built in default values
    """

    def __init__(self):
        self.name = "Room Name"
        self.description = "Room Desc"
        self.exits = []
        self.daemons = []
        self.cmds = {}


def dungeon(game=None):
    """
    Procedural Dungeon Generator
    Infinite Loop Warning: Do not directly iterate over.

    Takes the game as input, yields Room.
    """
    while True:
        room = Room()

        room.name = "CAVE SOMBRE"
        opennessRoll = random.randint(0, 3)
        if opennessRoll == 0:
            openness = "un labyrinthe sombre et exigu où il faut se faufiler entre tous les interstices de la roche"
        elif opennessRoll == 1:
            openness = "pas trop difficile de se faufiler, bien qu'il soit difficile de voir devant soi"
        elif opennessRoll == 2:
            openness = "un long couloir couvert de roches et de cristaux"
        else:
            openness = "une géode massive et ouverte à l'intérieur de laquelle vous vous tenez"

        wetnessRoll = random.randint(0, 3)
        if wetnessRoll == 0:
            wetness = "l'os sec en entendant le bruit de vos talons contre la roche dure en dessous"
        elif wetnessRoll == 1:
            wetness = "un peu humide car vous sentez le moût et la moisissure dans l'air"
        elif wetnessRoll == 2:
            wetness = "humide comme vous voyez l'eau s'infiltrer à travers les murs des grottes"
        else:
            wetness = "mouillé en pataugeant dans l'eau cristalline des grottes qui descend jusqu'aux chevilles"

        exitRoll = random.randint(0, 3)
        if exitRoll == 0:
            room.exits.append("nord")
        elif exitRoll == 1:
            room.exits.append("ouest")
        elif exitRoll == 2:
            room.exits.append("sud")
        else:
            room.exits.append("est")

        room.description = "Cette partie de la grotte est à {0} et {1}.\nSortie: {2}".format(openness, wetness,
                                                                                             ", ".join(room.exits))

        # Crystal Roll
        crystalRoll = random.randint(0, 6)
        if not crystalRoll:
            # The logic is really reversed
            # Think: if crystal
            room.description += "\nIl y a un cristal blanc brillant ici dans la pièce. La rumeur dit que si vous touchez un de ces cristaux, il vous guérira complètement, mais il prendra aussi le contrôle de votre esprit et vous fera rentrer chez vous en somnambule.\n\n"

            room.cmds = {"toucher cristal": game.warpHome,
                         "attraper cristal": game.warpHome,
                         "tc": game.warpHome()
                         }

        daemonRoll = random.randint(0, 3)
        if daemonRoll == 0:
            pass
        elif daemonRoll == 1:
            room.daemons.append(Daemon())
        elif daemonRoll == 2:
            room.daemons.append(Daemon())
        else:
            room.daemons.append(Daemon())
            room.daemons.append(Daemon())

        yield room


class Game(object):
    """
    Gameplay and functionality object
    Takes no inputs.
    Initializes on creation.
    Run with Game.run()
    """

    def __init__(self):
        self.character = None
        self.exit = False
        self.room = None
        self.dungeon = dungeon(self)
        self.safe = 0

    def run(self):
        """
        Game Loop
          Verify State
          Build Room
          Resolve Room
          Give Player Control
        """
        while not self.exit:
            # Verify Character
            #  Create New if no Character
            if not self.character:
                name = input("Quel est le nom de votre guerrier?\n>>> ")
                name = name.strip()
                testName = name.replace(" ", "").replace("'", "")
                if not testName.isalpha():
                    print("Attention: Le nom de votre guerrier doit contenir uniquement des lettres de l'alphabet")
                    continue

                self.character = Character(name)

            # Verify Room
            if not self.room:
                self.home()
                continue

            # Resolve Room
            self.look()
            self.combat()
            self.cleanup()

            # Resolve Character Death
            if not self.character:
                self.room = None
                continue

            # Player Input
            cmd = input(
                "{0} ~ P.V:{1}/{2} Att:{3} Def:{4} Or:{05}>>> ".format(self.character.name, self.character.health,
                                                                       self.character.maxHealth, self.character.attack,
                                                                       self.character.defense,
                                                                       self.character.gold))

            # Interpret Player CommandswarpHome
            cmd = cmd.strip()

            if cmd.lower() == "quitter":
                self.exit = True
            elif cmd.lower() in self.room.exits:
                self.room = next(self.dungeon)
            elif cmd.lower() == "tuer monstre" or cmd.lower() == "attaquer monstre" or cmd.lower() == "frapper monstre" or cmd.lower() == "balayer monstre" or cmd.lower() == "am":
                if self.room.daemons:
                    self.character.fight(self.room.daemons[0])
                else:
                    print("\n")
                    print("Attention: Il n'y a pas de monstre dans la pièce.")
                    print("\n")
            elif cmd.lower() in self.room.cmds:
                self.room.cmds[cmd.lower()]()
            elif cmd.lower() == "voir":
                continue

            else:
                print("Attention: Cette commande n'est pas reconnue.")

            print("\n")

    def combat(self):
        # Resolving when Daemons fight the Player
        for daemon in self.room.daemons:
            if daemon.aggression == 10:
                daemon.fight(self.character)
                self.character.fight(daemon)
            elif daemon.aggression > 4:
                coinFlip = random.randint(0, 1)
                if coinFlip:
                    daemon.fight(self.character)
                    daemon.aggression = 10
                    self.character.fight(daemon)

    def cleanup(self):
        """
        The game.cleanup Method is ran at the end of each game loop to resolve things like player and Daemon deaths. No inputs and it returns nothing.
        """
        # Character Death
        if self.character.health < 1:
            print("\n")
            print(
                "Désolé {0}, il semble que tu sois mort. Ton âme est maintenant entre les mains de Charon... s'il le juge bon.".format(
                    self.character.name))
            print("\n\n")
            print("Game Over")
            print("\n\n")
            self.character = None
            return

        # Daemon Death
        livingDaemons = []
        for daemon in self.room.daemons:
            if daemon.health < 1:
                if not self.character.weapon:
                    print(
                        "Ton coup de poing s'enfonce dans la poitrine du {0} avec un bruit sourd et creux, tandis que le cadavre tombe sur le sol et se consume dans un tourbillon de braises.".format(
                            daemon.name.lower()))
                    print(
                        "Wallah tu as tué {0} sale fou avec la patate du sheitan!".format(
                            daemon.name.lower()))
                    print("\n")
                else:
                    print(
                        "Ton {1} s'enfonce dans la poitrine du {0} avec un bruit sourd et un gargouillis, tandis que le cadavre se détache de ton {2} et se consume dans un tourbillon de braises.".format(
                            daemon.name.lower(), self.character.weapon.attType, self.character.weapon.name.lower()))
                    print(
                        "Subhanallah la PUISSANCE, tu as mélangé {0}".format(
                            daemon.name.lower())
                    )
                    print("\n")
                self.character.gold += daemon.gold
                self.character.score += 1
            else:
                livingDaemons.append(daemon)
        self.room.daemons = livingDaemons

    def look(self):
        """
        Display the current room to the Player

        No Inputs, No Return
        """
        print(self.room.name)
        print("\n")
        print(self.room.description)
        if self.room.daemons:
            print("\n")
            print("Monstre(s) présent(s): {0}".format(", ".join([d.name for d in self.room.daemons])))
        print("\n")

    def home(self):
        """
        game.home creates the default Home room for the game. It is ran whenever the Player warps home as well as at new character creation.
        """
        homeRoom = Room()
        homeRoom.name = "LA MAISON DE LA MADRE"
        homeRoom.description = "Vous voyez vos affaires éparpillées dans la maison de la daronne depuis la dernière fois que vous êtes parti à l'aventure. Il y a un petit poêle à bois dans un coin qui fait double emploi pour garder l'endroit chaud et nourri. Dans l'autre coin, il y a un coffre-fort où vous gardez vos biens les plus précieux, avec une collection de compteurs griffonnés au-dessus. À n'importe quel moment dans votre cabane, vous pouvez 'retirer' ou 'déposer' de l'or dans votre coffre. Vous avez gravé {0} marques pour les démons que vous avez tués. Ton ami fidèle dort sur ton canapé, comme toujours. Il vend des épées pour seulement 20 ors !\n\nSur le côté sud de la petite cabane se trouve la porte qui mène au labyrinthe d'un réseau de grottes appelé Elysium.\nSortie: sud".format(
            self.character.score)
        homeRoom.exits = ["sud"]
        homeRoom.cmds = {"déposer": self.deposit, "retirer": self.withdraw, "acheter": self.buySword,
                         "acheter epee": self.buySword, "epee": self.buySword}
        self.room = homeRoom

    def deposit(self):
        """
        game.deposit is used in the player's home to save money for later use, ie the player's character dying.
        """
        self.safe += self.character.gold
        self.character.gold = 0
        print("\n")
        print("Vous avez déposé {0} or dans votre coffre.".format(self.safe))
        print("\n")

    def withdraw(self):
        """
        game.withdraw is used is the player's home to withdraw money from the safe.
        """
        self.character.gold += self.safe
        self.safe = 0
        print("\n")
        print("Vous avez sorti {0} or de votre coffre.".format(self.character.gold))
        print("\n")

    def warpHome(self):
        """
        game.warpHome is used by the white crystals and is used to heal and teleport the player Home.bytes
        """
        self.character.health = self.character.maxHealth
        self.room = None

    def buySword(self):
        """
        game.buySword is used in the home room for the player to buy a copper sword.

        This function creates and equips the sword.
        """
        if not self.character.gold >= 20:
            print("\n")
            print(
                "Ton amigo de toujours prend un snap en se foutant de ta gueule parce que t'as pas assez d'oseille. Faut charbonner source: tqt")
            print("\n")
            return
        sword = Weapon("Epee qui coupe", "slash", 5)
        self.character.weapon = sword
        self.character.gold -= 20


Game().run()
