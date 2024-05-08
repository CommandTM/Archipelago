from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (region, entrances) in haikuRegions:
        # world.get_entrance(exit, player).connect(world.get_region(region, player))
        for (entrance) in entrances:
            world.get_entrance(entrance, player).connect(world.get_region(entrance.split(":")[1], player))


def createTwoWayEntrances():
    flippedExits = []
    for (region) in haikuRegions:
        for (exit) in haikuRegions[region]:
            flippedExits.append(exit.split(":")[1] + ":" + exit.split(":")[0])

    for (flippedExit) in flippedExits:
        haikuRegions[flippedExit.split(":")[0]].append(flippedExit)


# Region, List Of Exits
haikuRegions = {}
    # ("": ["", ""...]},
    {"Menu": ["Menu:G0"]},
    {"Train": []},
    {"G0": ["G0:G1", "G0:G13Up", "G0:G13Down"]},
    {"G1": ["G1:G2", "G1:G4"]},
    {"G2": ["G2:G3", "G2:G6", "G2:G14"]},
    {"G3": ["G3:G4"]},
    {"G4": []},
    {"G5": ["G5:G8"]},
    {"G6": ["G6:G5", "G6:G16"]},
    {"G7": []},
    {"G8": ["G8:G10", "G8:G19"]},
    {"G9": []},
    {"G10": ["G10:G7", "G10:G11"]},
    {"G11": ["G11:G12"]},
    {"G12": []},
    {"G13Up": ["G13Up:F1"]},
    {"G13Down": ["G13Down:G16"]},
    {"G14": ["G14:G17"]},
    {"G15": []},
    {"G16": ["G16:G18"]},
    {"G17": ["G17:G15"]},
    {"G18": ["G18:Train"]},
    {"G19": []},

    {"F1": ["F1:F2"]},
    {"F2": ["F2:F3", "F2:F4"]},
    {"F3": []},
    {"F4": ["F4:F5"]},
    {"F5": ["F5:C7"]},
    {"C1": ["C1:SUR2"]},
    {"C2": ["C2:C1"]},
    {"C3": ["C3:C2", "C3:C4", "C3:C6", "C3:C10", "C3:C17"]},
    {"C4": ["C4:C5"]},
    {"C5": []},
    {"C6": ["C6:C5"]},
    {"C7": ["C7:C3"]},
    {"C8": ["C8:C9", "C8:C29"]},
    {"C9": ["C9:C3"]},
    {"C10": []},
    {"C17": []},
    {"C27": ["C27:C8"]},
    {"C29": []},

    {"SUR2": ["SUR2:Offshore"]},

    {"Offshore": []}
}

#  Exit, Region
# mandatoryConnections = [
#     # ("", ""),
#     {"G0:G1", "G1"),
#     {"G0:G13Up", "G13Up"),
#     {"G0:G13Down", "G13Down"),
#     {"G1:G2", "G2"),
#     {"G1:G4", "G4"),
#     {"G2:G3", "G3"),
#     {"G2:G6", "G6"),
#     {"G2:G14", "G14"),
#     {"G3:G4", "G4"),
#     {"G5:G8", "G8"),
#     {"G6:G5", ""),
# ]
