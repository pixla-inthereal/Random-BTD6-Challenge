from random import choice, randint


def ran_hero():
    """Randomizes Hero"""
    heroes = [
        "Quincy",
        "Gwendolin",
        "Striker Jones",
        "Obyn Greenfoot",
        "Rosalia",
        "Captain Churchill",
        "Benjamin",
        "Pat Fusty",
        "Ezili",
        "Adora",
        "Etienne",
        "Sauda",
        "Admiral Brickell",
        "Psi",
        "Geraldo",
        "Corvus"
    ]

    ## 2/3 to get a hero, returns No hero if failed
    if randint(1, 3) != 1:
        return choice(heroes)
    return "No hero"


def ran_difficulty():
    """Randomizes Difficulty and Mode"""
    difficulties = [
        "Easy",
        "Medium",
        "Hard"
    ]
    modes = [
        "Standard",
        "Apopalypse",
        "Reverse",
        "Half Cash",
        "Double HP MOABs",
        "Alternate Bloons Rounds",
        "Impoppable",
        "CHIMPS"
    ]
    return choice(difficulties) + " - " + choice(modes)


def ran_map():
    """Randomizes Map"""
    maps = [
        "Monkey Meadow",
        "In the Loop",
        "Middle of the Road",
        "Tinkerton",
        "Tree Stump",
        "Town Center",
        "One Two Tree",
        "Scrapyard",
        "The Cabin",
        "Resort",
        "Skates",
        "Lotus Island",
        "Candy Falls",
        "Winter Park",
        "Carved",
        "Park Path",
        "Alpine Run",
        "Frozen Over",
        "Cubism",
        "Four Circles",
        "Hedge",
        "End of the Road",
        "Logs",
        "Luminous Cove",
        "Sulfur Springs",
        "Water Park",
        "Polyphemus",
        "Covered Garden",
        "Quarry",
        "Quiet Street",
        "Bloonarius Prime",
        "Balance",
        "Encrypted",
        "Bazaar",
        "Adora's Temple",
        "Spring Spring",
        "Kartsndarts",
        "Moon Landing",
        "Haunted",
        "Downstream",
        "Firing Range",
        "Cracked",
        "Streambed",
        "Chutes",
        "Rake",
        "Spice Islands",
        "Ancient Portal",
        "Castle Revenge",
        "Dark Path",
        "Erosion",
        "Midnight Mansion",
        "Sunken Columns",
        "X Factor",
        "Mesa",
        "Geared",
        "Spillway",
        "Cargo",
        "Pat's Pond",
        "Peninsula",
        "High Finance",
        "Another Brick",
        "Off the Coast",
        "Cornfield",
        "Underground",
        "Glacial Trail",
        "Dark Dungeons",
        "Sanctuary",
        "Ravine",
        "Flooded Valley",
        "Infernal",
        "Bloody Puddles",
        "Workshop",
        "Quad",
        "Dark Castle",
        "Muddy Puddles",
        "#OUCH"
    ]
    return choice(maps)


def ran_towers():
    """Randomizes Towers and Paths"""
    towers = [
        "Dart Monkey",
        "Boomerang Monkey",
        "Bomb Shooter",
        "Tack Shooter",
        "Ice Monkey",
        "Glue Gunner",
        "Sniper Monkey",
        "Monkey Sub",
        "Monkey Buccaneer",
        "Monkey Ace",
        "Heli Pilot",
        "Mortar Monkey",
        "Dartling Gunner",
        "Wizard Monkey",
        "Super Monkey",
        "Ninja Monkey",
        "Alchemist",
        "Druid",
        "Mermonkey",
        "Banana Farm",
        "Spike Factory",
        "Monkey Village",
        "Engineer Monkey",
        "Beast Handler"
    ]
    tower_list = ""

    ## chooses each tower and randomly determines paths
    for i in towers:
        ## 1/4 chance for any one tower to be included
        if randint(1,4) == 1:
            tower_list += i + ": " + str(randint(0, 5)) + "-" + str(randint(0, 5)) + "-" + str(randint(0, 5)) + "\n"

    ## runs code again in case zero towers are rolled
    if tower_list == "":
        tower_list = ran_towers()

    return tower_list


def ran_rounds():
    """Randomly Decides Rounds"""
    ## Always Round 1 Start, can go up to round 140
    return "Rounds 1-" + str(randint(1, 140))


def create_challenge():
    """Gets the other random functions and compiles them together"""
    challenge = (ran_map() + " || " + ran_difficulty() + "\n" +
                 ran_rounds() + "\n\n" +
                 ran_hero() + "\n" + ran_towers())
    return challenge


def main():
    ## Creates a text file with the challenge
    f = open("challenge.txt", "w")
    f.write(create_challenge())
    f.close()


if __name__ == "__main__":
    main()
