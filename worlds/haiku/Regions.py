from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (region) in haikuRegions.keys():
        # world.get_entrance(exit, player).connect(world.get_region(region, player))
        entrances = haikuRegions[region]
        for (entrance) in entrances:
            world.get_entrance(entrance, player).connect(world.get_region(entrance.split(":")[1], player))


def formConnectorName(connector) -> str:
    return connector[0] + ":" + connector[1]


def formReversedConnectorName(connector) -> str:
    return connector[1] + ":" + connector[0]


def createTwoWayEntrances():
    for (connector) in haikuConnectors:
        haikuRegions[connector[0]].append(formConnectorName(connector))
        haikuRegions[connector[1]].append(formReversedConnectorName(connector))


# Region, List Of Exits
haikuRegions = {
    # ("": ["", ""...],
    # region AW Regions
    "Menu": [],
    "Train": [],
    "G0": [],
    "G1": [],
    "G2": [],
    "G3": [],
    "G4": [],
    "G5": [],
    "G6": [],
    "G7": [],
    "G8": [],
    "G9": [],
    "G10": [],
    "G11": [],
    "G12": [],
    "G13Up": [],
    "G13Down": [],
    "G14": [],
    "G15": [],
    "G16": [],
    "G17": [],
    "G18": [],
    "G19": [],
    # endregion

    # region TLB Regions
    "F1": [],
    "F2": [],
    "F3": [],
    "F4": [],
    "F5": [],
    "C1": [],
    "C2": [],
    "C3": [],
    "C4": [],
    "C5": [],
    "C6": [],
    "C7": [],
    "C8": [],
    "C9": [],
    "C10": [],
    "C17": [],
    "C27": [],
    "C29": [],
    # endregion

    "SUR2": [],

    "Offshore": []
}

haikuConnectors = [
    # region AW Connectors
    ["Menu", "G0"],
    ["G0", "G1"],
    ["G0", "G13Up"],
    ["G0", "G13Down"],
    ["G1", "G2"],
    ["G1", "G4"],
    ["G2", "G3"],
    ["G2", "G6"],
    ["G2", "G14"],
    ["G3", "G4"],
    ["G5", "G8"],
    ["G5", "G6"],
    ["G6", "G16"],
    ["G7", "G10"],
    ["G8", "G10"],
    ["G8", "G19"],
    ["G10", "G11"],
    ["G11", "G12"],
    ["G13Up", "F1"],
    ["G13Down", "G16"],
    ["G14", "G17"],
    ["G15", "G17"],
    ["G16", "G18"],
    ["G18", "Train"],
    # endregion

    # region TLB Connectors
    ["F1", "F2"],
    ["F2", "F3"],
    ["F2", "F4"],
    ["F4", "F5"],
    ["F5", "C7"],
    ["C1", "SUR2"],
    ["C1", "C2"],
    ["C2", "C3"],
    ["C3", "C4"],
    ["C3", "C6"],
    ["C3", "C7"],
    ["C3", "C9"],
    ["C3", "C10"],
    ["C3", "C17"],
    ["C4", "C5"],
    ["C5", "C6"],
    ["C8", "C9"],
    ["C8", "C29"],
    ["C8", "C27"],
    # endregion

    ["SUR2", "Offshore"],
]

#  Exit, Region
# mandatoryConnections = [
#     # ("", ""),
#     "G0:G1", "G1"),
#     "G0:G13Up", "G13Up"),
#     "G0:G13Down", "G13Down"),
#     "G1:G2", "G2"),
#     "G1:G4", "G4"),
#     "G2:G3", "G3"),
#     "G2:G6", "G6"),
#     "G2:G14", "G14"),
#     "G3:G4", "G4"),
#     "G5:G8", "G8"),
#     "G6:G5", ""),
# ]
