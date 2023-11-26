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

    if self.options.dark_room_logic.value:
        set_rule(multiworld.get_entrance("AW-02=SW-01", player),
                 lambda state: state.has("Bulblet", player))

    set_rule(multiworld.get_entrance("IB-03=SW-01", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism", player)))
    if self.options.dark_room_logic.value:
        add_rule(multiworld.get_entrance("IB-03=SW-01", player),
                 lambda state: state.has("Bulblet", player))

    set_rule(multiworld.get_entrance("TLB-02=CC-01", player),
             lambda state: state.has("Power Bomb", player))

    set_rule(multiworld.get_entrance("IB-01=CC-01", player),
             lambda state: (state.has("String And Hook", player) and (state.has("Jump Boosters", player) or
                                                                      state.has("Electro-Magnetism"))))

    
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
    # region Sunken Wastes
    set_rule(multiworld.get_entrance("SW-01=SW-02", player),
             lambda state: state.has("Body Modifier", player))

    set_rule(multiworld.get_entrance("SW-02=SW-TW", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism", player)))

    set_rule(multiworld.get_entrance("SW-TW=SW-01", player),
             lambda state: state.can_reach("SW-TW", "Region", player))
    # endregion
    # region Central Core
    set_rule(multiworld.get_entrance("CC-01=CC-02 01", player),
             lambda state: state.has("Space Disruptor", player))

    set_rule(multiworld.get_entrance("CC-01=CC-02 02", player),
             lambda state: state.has("Body Modifier", player))

    set_rule(multiworld.get_entrance("CC-01=CC-03", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism")))

    set_rule(multiworld.get_entrance("CC-01=CC-04", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism")))

    set_rule(multiworld.get_entrance("CC-01=CC-05", player),
             lambda state: state.has("Power Bomb", player))

    set_rule(multiworld.get_entrance("CC-02=CC-03 01", player),
             lambda state: state.has("Body Modifier", player))

    set_rule(multiworld.get_entrance("CC-02=CC-03 02", player),
             lambda state: state.has("Body Modifier", player))

    set_rule(multiworld.get_entrance("CC-04=CC-01", player),
             lambda state: state.can_reach("CC-04", "Region", player))

    set_rule(multiworld.get_entrance("CC-05=CC-E", player),
             lambda state: state.has("Power Bomb", player))
    # endregion


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    return
