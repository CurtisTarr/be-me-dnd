import random

D6_LOWER = 1
D6_UPPER = 6
STAT_ROLLS = 4
STATS = ["Strength", "Dexterity", "Constitution",
         "Intelligence", "Wisdom", "Charisma"]
CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
           "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
RACES = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling",
         "Half-Orc", "Human", "Tiefling"]
FIRST_NAMES = "first-names"
LAST_NAMES = "last-names"


def roll_stat():
    rolls = []
    while len(rolls) < STAT_ROLLS:
        rolls.append(random.randint(D6_LOWER, D6_UPPER))
    rolls.sort(reverse=1)
    return rolls[1] + rolls[2] + rolls[3]


def roll_stats():
    stats = {}
    for stat in STATS:
        stats[stat] = roll_stat()
    return stats


def gen_race():
    return RACES[random.randint(0, len(RACES) - 1)]


def gen_class():
    return CLASSES[random.randint(0, len(CLASSES) - 1)]


def get_random_name_from_file(filename: str):
    names = []
    with open(filename) as file:
        for name in file:
            names.append(name)
    return names[random.randint(0, len(names) - 1)].strip().capitalize()


def gen_name():
    return (get_random_name_from_file(FIRST_NAMES) + " "
            + get_random_name_from_file(LAST_NAMES))


if __name__ == "__main__":
    print("> Be me %s" % gen_name())
    print("> %s %s" % (gen_race(), gen_class()))
    for stat, value in roll_stats().items():
        print("> %s: %d" % (stat, value))
