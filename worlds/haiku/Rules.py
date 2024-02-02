from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld


def setRules(self, multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("AW-01 > AW-02", player),
             lambda state: state.has("Electro-Magnetism", player))
    
    set_rule(multiworld.get_entrance("AW-03 > AW-05", player),
             lambda state: state.has("Electro-Magnetism", player) or state.has("Jump Boosters", player))


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    return
