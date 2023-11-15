from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (exit, region) in mandatoryConnections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# Region, List Of Exits
haikuRegions = [
    ("Menu", ["Haiku's Awakening"]),
    ("Traveling Town", ["Abandoned Wastes Train", "Central Core Train", "Pinion's Expanse Train", "Water Ducts Train",
                        "Factory Facility Train", "Sunken Wastes Train", "Forgotten Ruins Train",
                        "The Last Bunker Train"]),
    ("Abandoned Wastes", ["Trash Chute", "Oven Door", "Sunken Wastes Elevator"]),
    ("Central Core", ["Air Fryer", "Busted Roof", "Pinion's Elevator Of Doom", "The Sewers"]),
    ("Pinion's Expanse", []),
    ("Incinerator Burner", ["Midnight Snack"]),
    ("Water Ducts", ["Industry Leader Elevator"]),
    ("Ruined Surface", ["Catacomb"]),
    ("Factory Facility", ["Overheating Factory", "Pinion's Elevator Of Safety", "Factory Door",
                          "Pinion's Elevator Of Doom 2.0"]),
    ("Blazing Furnace", []),
    ("Sunken Wastes", ["The Midnight Greenhouse"]),
    ("Forgotten Ruins", ["Overgrown Sewers"]),
    ("The Last Bunker", ["Bunker Door"]),
    ("Bunker Bypass", ["Broken Elevator", "Bear Trap Alley"])
]

# Exit, Region
mandatoryConnections = [
    ("Haiku's Awakening", "Abandoned Wastes"),
    # region Train
    ("Abandoned Wastes Train", "Abandoned Wastes"),
    ("Central Core Train", "Central Core"),
    ("Pinion's Expanse Train", "Pinion's Expanse"),
    ("Water Ducts Train", "Water Ducts"),
    ("Factory Facility Train", "Traveling Town"),
    ("Sunken Wastes Train", "Factory Facility"),
    ("Forgotten Ruins Train", "Forgotten Ruins"),
    ("The Last Bunker Train", "The Last Bunker"),
    # endregion
    # region Abandoned Wastes
    ("Trash Chute", "Bunker Bypass"),
    ("Oven Door", "Incinerator Burner"),
    ("Sunken Wastes Elevator", "Sunken Wastes"),
    # endregion
    # region Bunker Bypass
    ("Broken Elevator", "The Last Bunker"),
    ("Bear Trap Alley", "Central Core"),
    # endregion
    # region Central Core
    ("Air Fryer", "Incinerator Burner"),
    ("Busted Roof", "The Last Bunker"),
    ("Pinion's Elevator Of Doom", "Pinion's Expanse"),
    ("The Sewers", "Water Ducts"),
    # endregion
    ("Midnight Snack", "Sunken Wastes"),
    ("The Midnight Greenhouse", "Forgotten Ruins"),
    ("Overgrown Sewers", "Water Ducts"),
    ("Industry Leader Elevator", "Factory Facility"),
    # region Factory Facility
    ("Overheating Factory", "Blazing Furnace"),
    ("Pinion's Elevator Of Safety", "Pinion's Expanse"),
    ("Factory Door", "Ruined Surface"),
    ("Pinion's Elevator Of Doom 2.0", "Pinion's Expanse"),
    # endregion
    ("Catacomb", "Factory Facility"),
    ("Bunker Door", "Ruined Surface")
]
