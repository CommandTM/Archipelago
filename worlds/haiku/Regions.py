from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (exit, region) in mandatoryConnections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# Region, List Of Exits
haikuRegions = [
    ("Menu", ["Haiku's Awakening"]),
    ("Traveling Town", []),
    ("Abandoned Wastes", ["Abandoned Wastes Train", "Trash Chute", "Oven Door", "Sunken Wastes Elevator"]),
    ("Central Core", ["Central Core Train", "Air Fryer", "Busted Roof", "Pinion's Elevator Of Doom", "The Sewers"]),
    ("Pinion's Expanse", ["Pinion's Expanse Train"]),
    ("Incinerator Burner", ["Midnight Snack"]),
    ("Water Ducts", ["Water Ducts Train", "Industry Leader Elevator"]),
    ("Ruined Surface", ["Catacomb"]),
    ("Factory Facility", ["Factory Facility Train", "Overheating Factory", "Pinion's Elevator Of Safety",
                          "Factory Door", "Pinion's Elevator Of Doom 2.0"]),
    ("Blazing Furnace", []),
    ("Sunken Wastes", ["Sunken Wastes Train", "The Midnight Greenhouse"]),
    ("Forgotten Ruins", ["Forgotten Ruins Train", "Overgrown Sewers"]),
    ("The Last Bunker", ["The Last Bunker Train", "Bunker Door"]),
    ("Bunker Bypass", ["Broken Elevator", "Bear Trap Alley"])
]

# Exit, Region
mandatoryConnections = [
    ("Haiku's Awakening", "Abandoned Wastes"),
    # region Train
    ("Abandoned Wastes Train", "Traveling Town"),
    ("Central Core Train", "Traveling Town"),
    ("Pinion's Expanse Train", "Traveling Town"),
    ("Water Ducts Train", "Traveling Town"),
    ("Factory Facility Train", "Traveling Town"),
    ("Sunken Wastes Train", "Traveling Town"),
    ("Forgotten Ruins Train", "Traveling Town"),
    ("The Last Bunker Train", "Traveling Town"),
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
