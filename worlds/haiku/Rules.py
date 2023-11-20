from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld


def setRules(self, multiworld: MultiWorld, player: int):
    # region Region Connections
    set_rule(multiworld.get_entrance("AW-01=TLB-01", player),
             lambda state: (state.has("Electro-Magnetism") or state.has("Jump Boosters")))

    set_rule(multiworld.get_entrance("AW-02=IB-02", player),
             lambda state: state.has("Heat Treatment", player))

    set_rule(multiworld.get_entrance("IB-01=AW-02", player),
             lambda state: state.can_reach("IB-01", "Region", player))
    # endregion
    # region Abandoned Wastes
    set_rule(multiworld.get_entrance("AW-01=AW-02 01", player),
             lambda state: (state.has("Electro-Magnetism", player) or
                            state.has("Jump Boosters", player)))

    set_rule(multiworld.get_entrance("AW-01=AW-02 02", player),
             lambda state: state.has("Rusted Key", player))

    set_rule(multiworld.get_entrance("AW-01=AW-03", player),
             lambda state: state.can_reach("AW-03", "Region", player))

    set_rule(multiworld.get_entrance("AW-01=AW-TG", player),
             lambda state: (state.has("Electro-Magnetism", player) or
                            state.has("Jump Boosters", player)))

    set_rule(multiworld.get_entrance("AW-02=AW-03", player),
             lambda state: state.has("Electro-Magnetism"))
    # endregion
    # region The Last Bunker
    set_rule(multiworld.get_entrance("TLB-01=TLB-03", player),
             lambda state: (state.has("Electro-Magnetism", player) and state.has("Jump Boosters", player)))

    set_rule(multiworld.get_entrance("TLB-02=TLB-03", player),
             lambda state: state.has("Jump Boosters", player))

    # Robin Is "Pretty Sure" About This Rule
    set_rule(multiworld.get_entrance("TLB-03=TLB-04", player),
             lambda state: state.has("String And Hook", player))

    set_rule(multiworld.get_entrance("TLB-03=TLB-05", player),
             lambda state: state.has("Space Disruptor", player))

    set_rule(multiworld.get_entrance("TLB-03=TLB-T", player),
             lambda state: (state.has("Body Modifier", player) and state.has("Power Bomb", player)))

    set_rule(multiworld.get_entrance("TLB-T=TLB-03", player),
             lambda state: state.can_reach("TLB-T", "Region", player))
    # endregion
    # region Incinerator Burner
    set_rule(multiworld.get_entrance("IB-01=IB-02", player),
             lambda state: (state.has("Electro-Magnetism", player) or state.has("Jump Boosters", player)))

    set_rule(multiworld.get_entrance("IB-02=IB-03", player),
             lambda state: (state.has("Electro-Magnetism", player) or state.has("Jump Boosters", player)))
    # endregion


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    return
