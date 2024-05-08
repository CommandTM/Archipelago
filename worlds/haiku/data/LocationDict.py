all_locations = {
    # region Abilities
    "Electro-Magnetism": "G7",
    "Body Modifier": "Menu",
    "Bulblet": "Menu",
    "Heat Treatment": "Menu",
    "Sealant Treatment": "Menu",
    "Jump Boosters": "Menu",
    "String And Hook": "Menu",
    "Space Disruptor": "Menu",
    "Power Bomb": "Menu",
    "Adjustable Wrench": "G1",
    # endregion
    # region Chips
    "Infinity Edge": "G13Up",
    "Electro-Emitter": "Menu",
    "Shock Wave": "Menu",
    "Shock Projectile": "Menu",
    "Electric Orbs": "Menu",
    "Self-Detonation": "Menu",
    "Quick Repair": "Menu",
    "Gyro-Accelerator": "Menu",
    "Sawblade": "Menu",
    "Coolant Soluble": "Menu",
    "Auto Modifier": "Menu",
    "Tungsten Steel": "SUR2",
    "Auto Repair": "Menu",
    "Extractor": "Menu",
    "Bulb Relation": "Menu",
    "Amplifying Transputer": "Menu",
    "Magnetic Footing": "Menu",
    "Space Disturbance": "Menu",
    "Nomad's Plate": "F5",
    "Heat Drive": "Menu",
    "Agile Alloy": "Train",
    "Sword Extension": "Train",
    "Pocket Magnet": "Train",
    "Protector's Capsule": "Train",
    "Ferromagnetic": "Train",
    "Map Sweeper": "Train",
    "Power Enhancer": "SUR2",
    "Power Processor": "Menu",
    # endregion
    # region Power Cells
    "Central Core: Power Cell 01": "Menu",
    "Central Core: Power Cell 02": "Menu",
    "Central Core: Power Cell 03": "Menu",
    "Central Core: Power Cell 04": "Menu",
    "Pinion's Expanse: Power Cell": "Menu",
    "Incinerator Burner: Power Cell 01": "Menu",
    "Incinerator Burner: Power Cell 02": "Menu",
    "Water Ducts: Power Cell 01": "Menu",
    "Water Ducts: Power Cell 02": "Menu",
    "Water Ducts: Power Cell 03": "Menu",
    "Ruined Surface: Power Cell": "SUR2",
    "Factory Facility: Power Cell 01": "Menu",
    "Factory Facility: Power Cell 02": "Menu",
    "Factory Facility: Power Cell 03": "Menu",
    "Factory Facility: Power Cell 04": "Menu",
    "Factory Facility: Power Cell 05": "Menu",
    "Blazing Furnace: Power Cell": "Menu",
    "Sunken Wastes: Power Cell": "Menu",
    "Forgotten Ruins: Power Cell 01": "Menu",
    "Forgotten Ruins: Power Cell 02": "Menu",
    "Forgotten Ruins: Power Cell 03": "Menu",
    "The Last Bunker: Power Cell 01": "Menu",
    "The Last Bunker: Power Cell 02": "F4",
    "The Last Bunker: Power Cell 03": "C10",
    # endregion
    # region Health Fragments
    "Abandoned Wastes: Health Fragment": "G15",
    "Central Core: Health Fragment": "Menu",
    "Quatern's Project: Health Fragment 01": "Menu",
    "Quatern's Project: Health Fragment 02": "Menu",
    "Pinion's Expanse: Health Fragment": "Menu",
    "Water Ducts: Health Fragment": "Menu",
    "Factory Facility: Health Fragment": "Menu",
    "Sunken Wastes: Health Fragment": "Menu",
    "Forgotten Ruins: Health Fragment": "Menu",
    "The Last Bunker: Health Fragment": "Menu",
    "Traveling Town: Health Fragment 01": "Train",
    "Traveling Town: Health Fragment 02": "Train",
    # endregion
    # region Rusty Keys
    "Abandoned Wastes: Rusty Key": "G1",
    "Traveling Town: Rusty Key": "Train",
    "Sunken Wastes: Rusty Key": "Menu",
    "Factory Facility: Rusty Key": "Menu",
    # endregion
    "Goldcrest Whistle": "G6",
    "Electric Key": "Menu",
    "Cassette Tape": "C29",
    "Green Skull": "Train",
    "Red Skull": "SUR2",
    # region Liquid Coolants
    "Water Ducts: Liquid Coolant": "Menu",
    "Blazing Furnace: Liquid Coolant": "Menu",
    "Sunken Wastes: Liquid Coolant": "Menu",
    # endregion
    # region Chip Sockets
    "Water Ducts: Blue Chip Socket": "Menu",
    "Blazing Furnace: Red Chip Socket": "Menu",
    "Forgotten Ruins: Green Chip Socket": "Menu",
    "Traveling Town: Red Chip Socket": "Train",
    "Traveling Town: Blue Chip Socket": "Train",
    # endregion
    # region Creators
    # "Electron": "CC-E",
    # "Proton": "Blazing Furnace",
    # "Neutron": "TLB-05"
    # endregion
    # region Map Disruptors
    # "Abandoned Wastes: Map Disruptor 01": "AW-05",
    # "Abandoned Wastes: Map Disruptor 02": "AW-03",
    # "Central Core: Map Disruptor 01": "CC-03",
    # "Central Core: Map Disruptor 02": "CC-05",
    # "Pinion's Expanse: Map Disruptor": "PE-01",
    # "Incinerator Burner: Map Disruptor": "IB-01",
    # "Water Ducts: Map Disruptor": "Water Ducts",
    # "Factory Facility: Map Disruptor 01": "Factory Facility",
    # "Factory Facility: Map Disruptor 02": "Factory Facility",
    # "Blazing Furnace: Map Disruptor": "Blazing Furnace",
    # "Sunken Wastes: Map Disruptor": "SW-01",
    # "Forgotten Ruins: Map Disruptor": "Forgotten Ruins",
    # "The Last Bunker: Map Disruptor 01": "TLB-02",
    # "The Last Bunker: Map Disruptor 02": "TLB-05",
    # endregion
    # region Train Stations
    # "Abandoned Wastes: Train Station": "AW-02",
    # "Central Core: Train Station": "CC-01",
    # "Pinion's Expanse: Train Station": "PE-01",
    # "Water Ducts: Train Station": "Water Ducts",
    # "Factory Facility: Train Station": "Factory Facility",
    # "Sunken Wastes: Train Station": "SW-01",
    # "Forgotten Ruins: Train Station": "Forgotten Ruins",
    # "The Last Bunker: Train Station": "TLB-03",
    # endregion
}

exclusionTable = {
    "wrench": {
        "Adjustable Wrench"
    },
    #"mapDisruptors": {
    #    "Abandoned Wastes: Map Disruptor 01",
    #    "Abandoned Wastes: Map Disruptor 02",
    #    "Central Core: Map Disruptor 01",
    #    "Central Core: Map Disruptor 02",
    #    "Pinion's Expanse: Map Disruptor",
    #    "Incinerator Burner: Map Disruptor",
    #    "Water Ducts: Map Disruptor",
    #    "Factory Facility: Map Disruptor 01",
    #    "Factory Facility: Map Disruptor 02",
    #    "Blazing Furnace: Map Disruptor",
    #    "Sunken Wastes: Map Disruptor",
    #    "Forgotten Ruins: Map Disruptor",
    #    "The Last Bunker: Map Disruptor 01",
    #    "The Last Bunker: Map Disruptor 02"
    #},
    #"trainStations": {
    #    "Abandoned Wastes: Train Station",
    #    "Central Core: Train Station",
    #    "Pinion's Expanse: Train Station",
    #    "Water Ducts: Train Station",
    #    "Factory Facility: Train Station",
    #    "Sunken Wastes: Train Station",
    #    "Forgotten Ruins: Train Station",
    #    "The Last Bunker: Train Station"
    #},
    "chipSockets": {
        "Water Ducts: Blue Chip Socket",
        "Blazing Furnace: Red Chip Socket",
        "Forgotten Ruins: Green Chip Socket",
        "Traveling Town: Red Chip Socket",
        "Traveling Town: BLue Chip Socket"
    }#,
    #creators": {
    #    "Electron",
    #    "Proton",
    #    "Neutron"
    #}
}
