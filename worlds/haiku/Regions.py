from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (exit, region) in mandatoryConnections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# Region, List Of Exits
haikuRegions = [
    # ("", ["", ""...]),
    ("Menu", ["Menu > AW-01"]),
    ("AW-01", ["AW-01 > AW-02", "AW-01 > AW-03", "AW-01 > AW-04"]),
    ("AW-02", []),
    ("AW-03", ["AW-03 > AW-05"]),
    ("AW-04", []),
    ("AW-05", [])
]

# Exit, Region
mandatoryConnections = [
    # ("", ""),
    ("Menu > AW-01", "AW-01"),
    ("AW-01 > AW-02", "AW-02"),
    ("AW-01 > AW-03", "AW-03"),
    ("AW-01 > AW-04", "AW-04"),
    ("AW-03 > AW-05", "AW-05")
]
