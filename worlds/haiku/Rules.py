from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld


def setRules(self, multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("G0:G13Up", player),
             lambda state: hasWall(self, state))

    set_rule(multiworld.get_entrance("G0:G13Down", player),
             lambda state: hasWallOrDouble(self, state))

    #set_rule(multiworld.get_entrance("G2:G6", player),
    #         lambda state: hasKeys(self, state, 1))

    set_rule(multiworld.get_entrance("G13Down:G16", player),
             lambda state: hasWallOrDouble(self, state))

    set_rule(multiworld.get_entrance("G14:G17", player),
             lambda state: hasWallOrDouble(self, state))


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    return


def hasWall(self, state) -> bool:
    return state.has("Electro-Magnetism", self.player)


def hasWallOrDouble(self, state) -> bool:
    return state.has("Electro-Magnetism", self.player) or state.has("Jump Boosters", self.player)


def hasKeys(self, state, count) -> bool:
    return state.count("Rusty Key", self.player) >= count
