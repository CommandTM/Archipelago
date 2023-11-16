from worlds.generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld


def setRules(self, multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("Trash Chute", player),
             lambda state: state.has("Electro-Magnetism", player))

    set_rule(multiworld.get_entrance("Oven Door", player),
             lambda state: (state.has("Heat Treatment", player) and state.has("Electro-Magnetism", player)))

    set_rule(multiworld.get_entrance("Sunken Wastes Elevator", player),
             lambda state: state.can_reach("Sunken Wastes", "Region", player))
    if self.options.dark_room_logic.value:
        add_rule(multiworld.get_entrance("Sunken Wastes Elevator", player),
                 lambda state: state.has("Bulblet", player))

    set_rule(multiworld.get_entrance("Broken Elevator", player),
             lambda state: (state.has("Electro-Magnetism", player) and
                            state.has("Jump Boosters", player)))

    set_rule(multiworld.get_entrance("Bear Trap Alley", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism", player)))

    set_rule(multiworld.get_entrance("Air Fryer", player),
             lambda state: state.has("Heat Treatment", player))

    set_rule(multiworld.get_entrance("Busted Roof", player),
             lambda state: state.has("Power Bomb", player))

    set_rule(multiworld.get_entrance("Pinion's Elevator Of Doom", player),
             lambda state: state.has("Body Modifier", player))

    set_rule(multiworld.get_entrance("Power Tower Way", player),
             lambda state: (state.has("Jump Boosters", player) or state.has("Electro-Magnetism", player)))

    set_rule(multiworld.get_entrance("The Sewers", player),
             lambda state: state.has("Sealant Treatment", player))

    set_rule(multiworld.get_entrance("Midnight Snack", player),
             lambda state: state.can_reach("Incinerator Burner", "Region", player))
    if self.options.dark_room_logic.value:
        add_rule(multiworld.get_entrance("Sunken Wastes Elevator", player),
                 lambda state: state.has("Bulblet", player))

    set_rule(multiworld.get_entrance("The Midnight Greenhouse", player),
             lambda state: state.has("Space Disruptor", player))
    if self.options.dark_room_logic.value:
        add_rule(multiworld.get_entrance("The Midnight Greenhouse", player),
                 lambda state: state.has("Bulblet", player))

    set_rule(multiworld.get_entrance("Overgrown Sewers", player),
             lambda state: state.has("Sealant Treatment", player))

    set_rule(multiworld.get_entrance("Industry Leader Elevator", player),
             lambda state: state.has("Sealant Treatment", player))

    set_rule(multiworld.get_entrance("Overheating Factory", player),
             lambda state: (state.has("Heat Treatment", player) and
                            state.has("Jump Boosters", player) and
                            state.has("Electro-Magnetism", player)))

    set_rule(multiworld.get_entrance("Pinion's Elevator Of Safety", player),
             lambda state: state.has("Electro-Magnetism", player))

    set_rule(multiworld.get_entrance("Bunker Door", player),
             lambda state: state.has("Jump Boosters", player))

    set_rule(multiworld.get_entrance("Factory Door", player),
             lambda state: state.has("Jump Boosters", player))

    set_rule(multiworld.get_entrance("Water Ducts Train", player),
             lambda state: state.has("Sealant Treatment", player))

    if self.options.train_stations.value:
        set_rule(multiworld.get_entrance("Abandoned Wastes Train", player),
                 lambda state: state.has("Abandoned Wastes: Train Station", player))

        set_rule(multiworld.get_entrance("Central Core Train", player),
                 lambda state: state.has("Central Core: Train Station", player))

        set_rule(multiworld.get_entrance("Pinion's Expanse Train", player),
                 lambda state: state.has("Pinion's Expanse: Train Station", player))

        add_rule(multiworld.get_entrance("Water Ducts Train", player),
                 lambda state: state.has("Water Ducts: Train Station", player))

        set_rule(multiworld.get_entrance("Factory Facility Train", player),
                 lambda state: state.has("Factory Facility: Train Station", player))

        set_rule(multiworld.get_entrance("Sunken Wastes Train", player),
                 lambda state: state.has("Sunken Wastes: Train Station", player))

        set_rule(multiworld.get_entrance("Forgotten Ruins Train", player),
                 lambda state: state.has("Forgotten Ruins: Train Station", player))

        set_rule(multiworld.get_entrance("The Last Bunker Train", player),
                 lambda state: state.has("The Last Bunker: Train Station", player))
    else:
        set_rule(multiworld.get_entrance("Abandoned Wastes Train", player),
                 lambda state: ((state.can_reach("Central Core", "Region", player) or
                                 state.can_reach("Pinion's Expanse", "Region", player) or
                                 state.can_reach("Water Ducts", "Region", player) or
                                 state.can_reach("Factory Facility", "Region", player) or
                                 state.can_reach("Sunken Wastes", "Region", player) or
                                 state.can_reach("Forgotten Ruins", "Region", player) or
                                 state.can_reach("The Last Bunker", "Region", player)) and
                                state.can_reach("Abandoned Wastes", "Region", player)))

        set_rule(multiworld.get_entrance("Central Core Train", player),
                 lambda state: state.can_reach("Central Core", "Region", player))

        set_rule(multiworld.get_entrance("Pinion's Expanse Train", player),
                 lambda state: state.can_reach("Pinion's Expanse", "Region", player))

        add_rule(multiworld.get_entrance("Water Ducts Train", player),
                 lambda state: state.can_reach("Water Ducts", "Region", player))

        set_rule(multiworld.get_entrance("Factory Facility Train", player),
                 lambda state: state.can_reach("Factory Facility", 'Region', player))

        set_rule(multiworld.get_entrance("Sunken Wastes Train", player),
                 lambda state: state.can_reach("Sunken Wastes", "Region", player))

        set_rule(multiworld.get_entrance("Forgotten Ruins Train", player),
                 lambda state: state.can_reach("Forgotten Ruins", "Region", player))

        set_rule(multiworld.get_entrance("The Last Bunker Train", player),
                 lambda state: state.can_reach("The Last Bunker", "Region", player))

    if self.options.dark_room_logic.value:
        add_rule(multiworld.get_entrance("Sunken Wastes Train", player),
                 lambda state: state.has("Bulblet", player))


def setCompletionRules(self, multiworld: MultiWorld, player: int):
    creatorsVirusEnding = lambda state: (state.can_reach("Central Core", "Region", player) and
                                         state.has("Proton", player) and
                                         state.has("Neutron", player) and
                                         state.has("Electron", player))
    
    noCreatorsVirusEnding = lambda state: (state.can_reach("Central Core", "Region", player) and
                                           state.can_reach("Blazing Furnace", "Region", player) and
                                           state.can_reach("The Last Bunker", "Region", player) and
                                           state.has("String And Hook", player))

    creatorsTrueEnding = lambda state: (state.can_reach("Central Core", "Region", player) and
                                        state.can_reach("Forgotten Ruins", "Region", player) and
                                        state.has("Proton", player) and
                                        state.has("Neutron", player) and
                                        state.has("Electron", player))

    noCreatorsTrueEnding = lambda state: (state.can_reach("Central Core", "Region", player) and
                                          state.can_reach("Blazing Furnace", "Region", player) and
                                          state.can_reach("The Last Bunker", "Region", player) and
                                          state.can_reach("Forgotten Ruins", "Region", player) and
                                          state.has("String And Hook", player))

    if self.options.ending.value == 0:
        if self.options.creators.value:
            multiworld.completion_condition[player] = lambda state: creatorsVirusEnding(state)
        else:
            multiworld.completion_condition[player] = lambda state: noCreatorsVirusEnding(state)
    elif self.options.ending.value == 1:
        if self.options.creators.value:
            multiworld.completion_condition[player] = lambda state: creatorsTrueEnding(state)
        else:
            multiworld.completion_condition[player] = lambda state: noCreatorsTrueEnding(state)
