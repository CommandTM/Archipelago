from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class CelesteAdvancement(Location):
    game: str = "Celeste"

    advancement_table = {
        "Forsaken City \"Start\" Berry 1": AdvData(69000000, "Forsaken City"),
        "Forsaken City \"Start\" Berry 2": AdvData(69000001, "Forsaken City"),
        "Forsaken City \"Start\" Berry 3": AdvData(69000002, "Forsaken City"),
        "Forsaken City \"Start\" Berry 4": AdvData(69000003, "Forsaken City"),
        "Forsaken City \"Start\" Berry 5": AdvData(69000004, "Forsaken City"),
        "Forsaken City \"Start\" Berry 6": AdvData(69000005, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 1": AdvData(69000006, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 2": AdvData(69000007, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 3": AdvData(69000008, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 4": AdvData(69000009, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 5": AdvData(69000010, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 6": AdvData(69000011, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 7": AdvData(69000012, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 8": AdvData(69000013, "Forsaken City"),
        "Forsaken City \"Crossing\" Berry 9": AdvData(69000014, "Forsaken City"),
        "Forsaken City \"Chasm\" Berry 1": AdvData(69000015, "Forsaken City"),
        "Forsaken City \"Chasm\" Berry 2": AdvData(69000016, "Forsaken City"),
        "Forsaken City \"Chasm\" Berry 3": AdvData(69000017, "Forsaken City"),
        "Forsaken City \"Chasm\" Berry 4": AdvData(69000018, "Forsaken City"),
        "Forsaken City \"Chasm\" Berry 5": AdvData(69000019, "Forsaken City"),
        "Forsaken City B-Side Cassette": AdvData(69000020, "Forsaken City"),
        "Pointless Machine": AdvData(69000021, "Forsaken City"),
        "Old Site \"Start\" Berry 1": AdvData(69000022, "Old Site"),
        "Old Site \"Start\" Berry 2": AdvData(69000023, "Old Site"),
        "Old Site \"Start\" Berry 3": AdvData(69000024, "Old Site"),
        "Old Site \"Start\" Berry 4": AdvData(69000025, "Old Site"),
        "Old Site \"Start\" Berry 5": AdvData(69000026, "Old Site"),
        "Old Site \"Start\" Berry 6": AdvData(69000027, "Old Site"),
        "Old Site \"Start\" Berry 7": AdvData(69000028, "Old Site"),
        "Old Site \"Start\" Berry 8": AdvData(69000029, "Old Site"),
        "Old Site \"Start\" Berry 9": AdvData(69000030, "Old Site"),
        "Old Site B-Side Cassette": AdvData(69000031, "Old Site"),
        "Old Site \"Intervention\" Berry 1": AdvData(69000032, "Old Site"),
        "Old Site \"Intervention\" Berry 2": AdvData(69000033, "Old Site"),
        "Old Site \"Intervention\" Berry 3": AdvData(69000034, "Old Site"),
        "Old Site \"Intervention\" Berry 4": AdvData(69000035, "Old Site"),
        "Old Site \"Intervention\" Berry 5": AdvData(69000036, "Old Site"),
        "Old Site \"Intervention\" Berry 6": AdvData(69000037, "Old Site"),
        "Old Site \"Intervention\" Berry 7": AdvData(69000038, "Old Site"),
        "Old Site \"Intervention\" Berry 8": AdvData(69000039, "Old Site"),
        "Old Site \"Awake\" Berry": AdvData(69000040, "Old Site"),
        "Resurrections": AdvData(69000041, "Old Site")
    }