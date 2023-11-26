from BaseClasses import MultiWorld


def linkHaikuAreas(world: MultiWorld, player: int):
    for (exit, region) in mandatoryConnections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# Region, List Of Exits
haikuRegions = [
    # ("", []),
    # region Abandoned Wastes
    ("Menu", ["Menu=AW-01"]),
    ("AW-01", ["AW-01=AW-02 01", "AW-01=AW-02 02", "AW-01=AW-03", "AW-01=AW-TG", "AW-01=TLB-01"]),
    ("AW-02", ["AW-02=AW-03", "AW-02=IB-02", "AW-02=SW-01"]),
    ("AW-03", []),
    ("AW-TG", []),
    # endregion
    # region The Last Bunker
    ("TLB-01", ["TLB-01=TLB-03", "TLB-01=CC-01"]),
    ("TLB-02", ["TLB-02=TLB-03", "TLB-02=CC-01"]),
    ("TLB-03", ["TLB-03=TLB-04", "TLB-03=TLB-05", "TLB-03=TLB-T", "TLB-03=RS-01"]),
    ("TLB-04", []),
    ("TLB-05", []),
    ("TLB-T", ["TLB-T=TLB-03"]),
    # endregion
    ("RS-01", []),
    # region Incinerator Burner
    ("IB-01", ["IB-01=IB-02", "IB-01=AW-02", "IB-01=CC-01"]),
    ("IB-02", ["IB-02=IB-03", "IB-02=CC-01"]),
    ("IB-03", ["IB-03=SW-01", "IB-03=CC-05"]),
    # endregion
    # region Sunken Wastes
    ("SW-01", ["SW-01=SW-02"]),
    ("SW-02", ["SW-02=SW-TW"]),
    ("SW-TW", ["SW-TW=SW-01"]),
    # endregion
    # region Central Core
    ("CC-01", ["CC-01=CC-02 01", "CC-01=CC-02 02", "CC-01=CC-03", "CC-01=CC-QP", "CC-01=CC-04", "CC-01=CC-05"]),
    ("CC-02", ["CC-02=CC-03 01", "CC-02=CC-03 02"]),
    ("CC-03", []),
    ("CC-04", ["CC-04=CC-01", "CC-04=PE-01"]),
    ("CC-05", ["CC-05=CC-E"]),
    ("CC-QP", []),
    ("CC-E", []),
    # endregion
    ("PE-01", []),
]

# Exit, Region
mandatoryConnections = [
    # ("", ""),
    # region Region Connections
    ("AW-01=TLB-01", "TLB-01"),
    ("AW-02=IB-02", "IB-02"),
    ("IB-01=AW-02", "AW-02"),
    ("AW-02=SW-01", "SW-01"),
    ("IB-03=SW-01", "SW-01"),
    # endregion
    # region Abandoned Wastes
    ("Menu=AW-01", "AW-01"),
    ("AW-01=AW-02 01", "AW-02"),
    ("AW-01=AW-02 02", "AW-02"),
    ("AW-01=AW-03", "AW-03"),
    ("AW-01=AW-TG", "AW-TG"),
    ("AW-02=AW-03", "AW-03"),
    # endregion
    # region The Last Bunker
    ("TLB-01=TLB-03", "TLB-03"),
    ("TLB-02=TLB-03", "TLB-03"),
    ("TLB-03=TLB-04", "TLB-04"),
    ("TLB-03=TLB-05", "TLB-05"),
    ("TLB-03=TLB-T", "TLB-T"),
    ("TLB-T=TLB-03", "TLB-03"),
    ("TLB-03=RS-01", "RS-01"),
    # endregion
    # region Incinerator Burner
    ("IB-01=IB-02", "IB-02"),
    ("IB-02=IB-03", "IB-03"),
    # endregion
    # region Sunken Wastes
    ("SW-01=SW-02", "SW-02"),
    ("SW-02=SW-TW", "SW-TW"),
    ("SW-TW=SW-01", "SW-01"),
    # endregion
    # region Central Core
    ("CC-01=CC-02 01", "CC-02"),
    ("CC-01=CC-02 02", "CC-02"),
    ("CC-01=CC-03", "CC-03"),
    ("CC-01=CC-QP", "CC-QP"),
    ("CC-01=CC-04", "CC-04"),
    ("CC-01=CC-05", "CC-05"),
    ("CC-02=CC-03 01", "CC-03"),
    ("CC-02=CC-03 02", "CC-03"),
    ("CC-05=CC-E", "CC-E")
    # endregion
]
