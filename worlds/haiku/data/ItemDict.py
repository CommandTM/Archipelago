from BaseClasses import ItemClassification

all_items = {
    # region Abilities
    "Electro-Magnetism": ItemClassification.progression,
    "Body Modifier": ItemClassification.progression,
    "Bulblet": ItemClassification.progression,
    "Heat Treatment": ItemClassification.progression,
    "Sealant Treatment": ItemClassification.progression,
    "Jump Boosters": ItemClassification.progression,
    "String And Hook": ItemClassification.progression,
    "Space Disruptor": ItemClassification.progression,
    "Power Bomb": ItemClassification.progression,
    "Adjustable Wrench": ItemClassification.useful,
    "Goldcrest Whistle": ItemClassification.useful,
    # endregion
    # region Chips
    "Infinity Edge": ItemClassification.useful,
    "Electro-Emitter": ItemClassification.useful,
    "Shock Wave": ItemClassification.useful,
    "Shock Projectile": ItemClassification.useful,
    "Electric Orbs": ItemClassification.useful,
    "Self-Detonation": ItemClassification.useful,
    "Quick Repair": ItemClassification.useful,
    "Gyro-Accelerator": ItemClassification.useful,
    "Sawblade": ItemClassification.useful,
    "Coolant Soluble": ItemClassification.useful,
    "Auto Modifier": ItemClassification.useful,
    "Tungsten Steel": ItemClassification.useful,
    "Auto Repair": ItemClassification.useful,
    "Extractor": ItemClassification.useful,
    "Bulb Relation": ItemClassification.useful,
    "Amplifying Transputer": ItemClassification.useful,
    "Magnetic Footing": ItemClassification.useful,
    "Space Disturbance": ItemClassification.useful,
    "Nomad's Plate": ItemClassification.useful,
    "Heat Drive": ItemClassification.useful,
    "Agile Alloy": ItemClassification.useful,
    "Sword Extension": ItemClassification.useful,
    "Pocket Magnet": ItemClassification.useful,
    "Protector's Capsule": ItemClassification.useful,
    "Ferromagnetic": ItemClassification.useful,
    "Map Sweeper": ItemClassification.useful,
    "Power Enhancer": ItemClassification.useful,
    "Power Processor": ItemClassification.useful,
    # endregion
    # region Map Disruptors
    "Abandoned Wastes: Map Disruptor 01": ItemClassification.useful,
    "Abandoned Wastes: Map Disruptor 02": ItemClassification.useful,
    "Central Core: Map Disruptor 01": ItemClassification.useful,
    "Central Core: Map Disruptor 02": ItemClassification.useful,
    "Pinion's Expanse: Map Disruptor": ItemClassification.useful,
    "Incinerator Burner: Map Disruptor": ItemClassification.useful,
    "Water Ducts: Map Disruptor": ItemClassification.useful,
    "Factory Facility: Map Disruptor 01": ItemClassification.useful,
    "Factory Facility: Map Disruptor 02": ItemClassification.useful,
    "Blazing Furnace: Map Disruptor": ItemClassification.useful,
    "Sunken Wastes: Map Disruptor": ItemClassification.useful,
    "Forgotten Ruins: Map Disruptor": ItemClassification.useful,
    "The Last Bunker: Map Disruptor 01": ItemClassification.useful,
    "The Last Bunker: Map Disruptor 02": ItemClassification.useful,
    # endregion
    # region Train Stations
    "Abandoned Wastes: Train Station": ItemClassification.useful,
    "Central Core: Train Station": ItemClassification.useful,
    "Pinion's Expanse: Train Station": ItemClassification.useful,
    "Water Ducts: Train Station": ItemClassification.useful,
    "Factory Facility: Train Station": ItemClassification.useful,
    "Sunken Wastes: Train Station": ItemClassification.useful,
    "Forgotten Ruins: Train Station": ItemClassification.useful,
    "The Last Bunker: Train Station": ItemClassification.useful,
    # endregion
    # region Various
    "Power Cell": ItemClassification.useful,
    "Health Fragment": ItemClassification.useful,
    "Rusted Key": ItemClassification.useful,
    "Electric Key": ItemClassification.useful,
    "Cassette Tape": ItemClassification.useful,
    "Green Skull": ItemClassification.useful,
    "Red Skull": ItemClassification.useful,
    "Liquid Coolant": ItemClassification.useful,
    # region Chip Sockets
    "Red Chip Socket": ItemClassification.useful,
    "Blue Chip Socket": ItemClassification.useful,
    "Green Chip Socket": ItemClassification.useful,
    # endregion
    # region Creators
    "Electron": ItemClassification.progression,
    "Proton": ItemClassification.progression,
    "Neutron": ItemClassification.progression,
    # endregion
    # region Money
    "$10": ItemClassification.filler,
    "$50": ItemClassification.filler,
    "$100": ItemClassification.filler
    # endregion
    # endregion
}

# Frequency Tables
necessaryItems = {
    "Electro-Magnetism": 1,
    "Body Modifier": 1,
    "Bulblet": 1,
    "Heat Treatment": 1,
    "Sealant Treatment": 1,
    "Jump Boosters": 1,
    "String And Hook": 1,
    "Space Disruptor": 1,
    "Power Bomb": 1,
    "Goldcrest Whistle": 1,
    "Infinity Edge": 1,
    "Electro-Emitter": 1,
    "Shock Wave": 1,
    "Shock Projectile": 1,
    "Electric Orbs": 1,
    "Self-Detonation": 1,
    "Quick Repair": 1,
    "Gyro-Accelerator": 1,
    "Sawblade": 1,
    "Coolant Soluble": 1,
    "Auto Modifier": 1,
    "Tungsten Steel": 1,
    "Auto Repair": 1,
    "Extractor": 1,
    "Bulb Relation": 1,
    "Amplifying Transputer": 1,
    "Magnetic Footing": 1,
    "Space Disturbance": 1,
    "Nomad's Plate": 1,
    "Heat Drive": 1,
    "Agile Alloy": 1,
    "Sword Extension": 1,
    "Pocket Magnet": 1,
    "Protector's Capsule": 1,
    "Ferromagnetic": 1,
    "Map Sweeper": 1,
    "Power Enhancer": 1,
    "Power Processor": 1,
    "Power Cell": 24,
    "Health Fragment": 10,
    "Rusted Key": 4,
    "Electric Key": 1,
    "Cassette Tape": 1,
    "Green Skull": 1,
    "Red Skull": 1,
    "Liquid Coolant": 3
}

mapDisruptors = {
    "Abandoned Wastes: Map Disruptor 01": 1,
    "Abandoned Wastes: Map Disruptor 02": 1,
    "Central Core: Map Disruptor 01": 1,
    "Central Core: Map Disruptor 02": 1,
    "Pinion's Expanse: Map Disruptor": 1,
    "Incinerator Burner: Map Disruptor": 1,
    "Water Ducts: Map Disruptor": 1,
    "Factory Facility: Map Disruptor 01": 1,
    "Factory Facility: Map Disruptor 02": 1,
    "Blazing Furnace: Map Disruptor": 1,
    "Sunken Wastes: Map Disruptor": 1,
    "Forgotten Ruins: Map Disruptor": 1,
    "The Last Bunker: Map Disruptor 01": 1,
    "The Last Bunker: Map Disruptor 02": 1
}

trainStations = {
    "Abandoned Wastes: Train Station": 1,
    "Central Core: Train Station": 1,
    "Pinion's Expanse: Train Station": 1,
    "Water Ducts: Train Station": 1,
    "Factory Facility: Train Station": 1,
    "Sunken Wastes: Train Station": 1,
    "Forgotten Ruins: Train Station": 1,
    "The Last Bunker: Train Station": 1
}

chipSockets = {
    "Red Chip Socket": 2,
    "Blue Chip Socket": 2,
    "Green Chip Socket": 1
}

creators = {
    "Electron": 1,
    "Proton": 1,
    "Neutron": 1
}

junkWeights = {
    "$10": 10,
    "$50": 5,
    "$100": 1
}
