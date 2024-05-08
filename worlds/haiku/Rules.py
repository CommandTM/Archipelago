from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld


def setRules(self, multiworld: MultiWorld, player: int):
    region_rules = {
        "G0:G13Up": lambda state: hasWall(self, state),
        "G0:G13Down": lambda state: hasWallOrDouble(self, state),
        "G2:G6": lambda state: hasKeys(self, state, 1),
        "G8:G19": lambda state: hasLight(self, state),
        "G10:G11": lambda state: hasWall(self, state),
        "G13Down:G16": lambda state: hasWallOrDouble(self, state),
        "G14:G17": lambda state: hasWallOrDouble(self, state),
        "F1:F2": lambda state: hasWall(self, state),
        "F2:F3": lambda state: hasWall(self, state),
        "F2:F4": lambda state: hasWall(self, state),
        "F4:F5": lambda state: hasWallOrDouble(self, state),
        "F5:C7": lambda state: hasWallAndDouble(self, state),
        "C1:SUR2": lambda state: sealantTreated(self, state) and hasLight(self, state),
        "C2:C3": lambda state: hasWallOrDouble(self, state),
        "C3:C4": lambda state: hasWallOrDouble(self, state),
        "C3:C6": lambda state: hasWallOrDouble(self, state),
        "C3:C10": lambda state: hasWallOrDouble(self, state),
        "C3:C17": lambda state: hasWall(self, state) and (hasDouble(self, state) or hasHook(self, state)),
        "C4:C5": lambda state: hasWallOrDouble(self, state),
        "C8:C9": lambda state: hasWallAndDouble(self, state) or (hasWall(self, state) and hasHook(self, state)),
        "C8:C29": lambda state: hasWallAndDouble(self, state) or (hasWall(self, state) and hasHook(self, state)),
        "C8:C27": lambda state: hasWall(self, state),

    }

    location_rules = {
        "Electro-Magnetism": lambda state: hasWall(self, state),
        "The Last Bunker: Power Cell 02": lambda state: hasWallOrDouble(self, state),
        "The Last Bunker: Power Cell 03": lambda state: hasWallOrDouble(self, state) and hasHook(self, state),
    }

    for rule in region_rules.keys():
        set_rule(multiworld.get_entrance(rule, player), region_rules[rule])
        set_rule(multiworld.get_entrance(flipRegionName(rule), player), region_rules[rule])

    for rule in location_rules.keys():
        set_rule(multiworld.get_location(rule, player), location_rules[rule])


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    return


def flipRegionName(name) -> str:
    return name.split(":")[1] + ":" + name.split(":")[0]


def hasWall(self, state) -> bool:
    return state.has("Electro-Magnetism", self.player)


def hasDouble(self, state) -> bool:
    return state.has("Jump Boosters", self.player)


def hasHook(self, state) -> bool:
    return state.has("String And Hook", self.player)


def hasLight(self, state) -> bool:
    return state.has("Bulblet", self.player)


def sealantTreated(self, state) -> bool:
    return state.has("Sealant Treatment", self.player)


def hasWallOrDouble(self, state) -> bool:
    return hasWall(self, state) or hasDouble(self, state)


def hasWallAndDouble(self, state) -> bool:
    return hasWall(self, state) and hasDouble(self, state)


def hasKeys(self, state, count) -> bool:
    return state.count("Rusty Key", self.player) >= count
