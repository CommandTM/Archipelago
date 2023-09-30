from BaseClasses import Location
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

class CelesteAdvancement(Location):
    game: str = "Celeste"

advancement_table = {
    # Forsaken City 69000000-69000021
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

    # Old Site 69000022-69000041
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
    "Resurrections": AdvData(69000041, "Old Site"),

    #Celestial Resort 69000042-69000068
    "Celestial Resort \"Start\" Berry 1": AdvData(69000042, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 2": AdvData(69000043, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 3": AdvData(69000044, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 4": AdvData(69000045, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 5": AdvData(69000046, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 6": AdvData(69000047, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 7": AdvData(69000048, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 8": AdvData(69000049, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 9": AdvData(69000050, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 10": AdvData(69000051, "Celestial Resort"),
    "Celestial Resort \"Start\" Berry 11": AdvData(69000052, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 1": AdvData(69000053, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 2": AdvData(69000054, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 3": AdvData(69000055, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 4": AdvData(69000056, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 5": AdvData(69000057, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 6": AdvData(69000058, "Celestial Resort"),
    "Celestial Resort \"Huge Mess\" Berry 7": AdvData(69000059, "Celestial Resort"),
    "Celestial Resort \"Elevator Shaft\" Berry 1": AdvData(69000060, "Celestial Resort"),
    "Celestial Resort \"Elevator Shaft\" Berry 2": AdvData(69000061, "Celestial Resort"),
    "Celestial Resort \"Elevator Shaft\" Berry 3": AdvData(69000062, "Celestial Resort"),
    "Celestial Resort \"Elevator Shaft\" Berry 4": AdvData(69000063, "Celestial Resort"),
    "Celestial Resort B-Side Cassette": AdvData(69000064, "Celestial Resort"),
    "Celestial Resort \"Presidential Suite\" Berry 1": AdvData(69000065, "Celestial Resort"),
    "Celestial Resort \"Presidential Suite\" Berry 2": AdvData(69000066, "Celestial Resort"),
    "Celestial Resort \"Presidential Suite\" Berry 3": AdvData(69000067, "Celestial Resort"),
    "Scattered And Lost": AdvData(69000068, "Celestial Resort"),

    # Golden Ridge 69000069-69000099
    "Golden Ridge \"Start\" Berry 1": AdvData(69000069, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 2": AdvData(69000070, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 3": AdvData(69000071, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 4": AdvData(69000072, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 5": AdvData(69000073, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 6": AdvData(69000074, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 7": AdvData(69000075, "Golden Ridge"),
    "Golden Ridge \"Start\" Berry 8": AdvData(69000076, "Golden Ridge"),
    "Golden Ridge B-Side Cassette": AdvData(69000077, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 1": AdvData(69000078, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 2": AdvData(69000079, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 3": AdvData(69000080, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 4": AdvData(69000081, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 5": AdvData(69000082, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 6": AdvData(69000083, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 7": AdvData(69000084, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 8": AdvData(69000085, "Golden Ridge"),
    "Golden Ridge \"Shrine\" Berry 9": AdvData(69000086, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 1": AdvData(69000087, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 2": AdvData(69000088, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 3": AdvData(69000089, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 4": AdvData(69000090, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 5": AdvData(69000091, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 6": AdvData(69000092, "Golden Ridge"),
    "Golden Ridge \"Old Trail\" Berry 7": AdvData(69000093, "Golden Ridge"),
    "Golden Ridge \"Cliff Face\" Berry 1": AdvData(69000094, "Golden Ridge"),
    "Golden Ridge \"Cliff Face\" Berry 2": AdvData(69000095, "Golden Ridge"),
    "Golden Ridge \"Cliff Face\" Berry 3": AdvData(69000096, "Golden Ridge"),
    "Golden Ridge \"Cliff Face\" Berry 4": AdvData(69000097, "Golden Ridge"),
    "Golden Ridge \"Cliff Face\" Berry 5": AdvData(69000098, "Golden Ridge"),
    "Eye Of The Storm": AdvData(69000099, "Golden Ridge"),

    # Mirror Temple 69000100-69000132
    "Mirror Temple \"Start\" Berry 1": AdvData(69000100, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 2": AdvData(69000101, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 3": AdvData(69000102, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 4": AdvData(69000103, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 5": AdvData(69000104, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 6": AdvData(69000105, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 7": AdvData(69000106, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 8": AdvData(69000107, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 9": AdvData(69000108, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 10": AdvData(69000109, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 11": AdvData(69000110, "Mirror Temple"),
    "Mirror Temple \"Start\" Berry 12": AdvData(69000111, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 1": AdvData(69000112, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 2": AdvData(69000113, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 3": AdvData(69000114, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 4": AdvData(69000115, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 5": AdvData(69000116, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 6": AdvData(69000117, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 7": AdvData(69000118, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 8": AdvData(69000119, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 9": AdvData(69000120, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 10": AdvData(69000121, "Mirror Temple"),
    "Mirror Temple \"Depths\" Berry 11": AdvData(69000122, "Mirror Temple"),
    "Mirror Temple B-Side Cassette": AdvData(69000123, "Mirror Temple"),
    "Mirror Temple \"Unravelling\" Berry": AdvData(69000124, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 1": AdvData(69000125, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 2": AdvData(69000126, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 3": AdvData(69000127, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 4": AdvData(69000128, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 5": AdvData(69000129, "Mirror Temple"),
    "Mirror Temple \"Search\" Berry 6": AdvData(69000130, "Mirror Temple"),
    "Mirror Temple \"Rescue\" Berry": AdvData(69000131, "Mirror Temple"),
    "Quiet And Falling": AdvData(69000132, "Mirror Temple"),

    # Reflection 69000133-69000134
    "Reflections B-Side Cassette": AdvData(69000133, "Reflections"),
    "Heavy And Frail": AdvData(69000134, "Reflections"),

    # Summit 69000135-69000189
    "Summit \"Start\" Berry 1": AdvData(69000135, "Summit"),
    "Summit \"Start\" Berry 2": AdvData(69000136, "Summit"),
    "Summit \"Start\" Berry 3": AdvData(69000137, "Summit"),
    "Summit \"Start\" Berry 4": AdvData(69000138, "Summit"),
    "Summit \"500M\" Berry 1": AdvData(69000139, "Summit"),
    "Summit \"500M\" Berry 2": AdvData(69000140, "Summit"),
    "Summit \"500M\" Berry 3": AdvData(69000141, "Summit"),
    "Summit \"500M\" Berry 4": AdvData(69000142, "Summit"),
    "Summit \"500M\" Berry 5": AdvData(69000143, "Summit"),
    "Summit \"500M\" Berry 6": AdvData(69000144, "Summit"),
    "Summit \"1000M\" Berry 1": AdvData(69000145, "Summit"),
    "Summit \"1000M\" Berry 2": AdvData(69000146, "Summit"),
    "Summit \"1000M\" Berry 3": AdvData(69000147, "Summit"),
    "Summit \"1000M\" Berry 4": AdvData(69000148, "Summit"),
    "Summit \"1000M\" Berry 5": AdvData(69000149, "Summit"),
    "Summit \"1000M\" Berry 6": AdvData(69000150, "Summit"),
    "Summit \"1500M\" Berry 1": AdvData(69000151, "Summit"),
    "Summit \"1500M\" Berry 2": AdvData(69000152, "Summit"),
    "Summit \"1500M\" Berry 3": AdvData(69000153, "Summit"),
    "Summit \"1500M\" Berry 4": AdvData(69000154, "Summit"),
    "Summit \"1500M\" Berry 5": AdvData(69000155, "Summit"),
    "Summit \"1500M\" Berry 6": AdvData(69000156, "Summit"),
    "Summit \"1500M\" Berry 7": AdvData(69000157, "Summit"),
    "Summit \"1500M\" Berry 8": AdvData(69000158, "Summit"),
    "Summit B-Side Cassette": AdvData(69000159, "Summit"),
    "Summit \"2000M\" Berry 1": AdvData(69000160, "Summit"),
    "Summit \"2000M\" Berry 2": AdvData(69000161, "Summit"),
    "Summit \"2000M\" Berry 3": AdvData(69000162, "Summit"),
    "Summit \"2000M\" Berry 4": AdvData(69000163, "Summit"),
    "Summit \"2000M\" Berry 5": AdvData(69000164, "Summit"),
    "Summit \"2000M\" Berry 6": AdvData(69000165, "Summit"),
    "Summit \"2000M\" Berry 7": AdvData(69000166, "Summit"),
    "Summit \"2000M\" Berry 8": AdvData(69000167, "Summit"),
    "Summit \"2500M\" Berry 1": AdvData(69000168, "Summit"),
    "Summit \"2500M\" Berry 2": AdvData(69000169, "Summit"),
    "Summit \"2500M\" Berry 3": AdvData(69000170, "Summit"),
    "Summit \"2500M\" Berry 4": AdvData(69000171, "Summit"),
    "Summit \"2500M\" Berry 5": AdvData(69000172, "Summit"),
    "Summit \"2500M\" Berry 6": AdvData(69000173, "Summit"),
    "Summit \"2500M\" Berry 7": AdvData(69000174, "Summit"),
    "Summit \"2500M\" Berry 8": AdvData(69000175, "Summit"),
    "Summit \"3000M\" Berry 1": AdvData(69000176, "Summit"),
    "Summit \"3000M\" Berry 2": AdvData(69000177, "Summit"),
    "Summit \"3000M\" Berry 3": AdvData(69000178, "Summit"),
    "Summit \"3000M\" Berry 4": AdvData(69000179, "Summit"),
    "Summit \"3000M\" Berry 5": AdvData(69000180, "Summit"),
    "Summit \"3000M\" Berry 6": AdvData(69000181, "Summit"),
    "Summit \"3000M\" Berry 7": AdvData(69000182, "Summit"),
    "Pink Sunrise": AdvData(69000183, "Summit")
    }

tape_locations = {
    "Forsaken City B-Side Cassette",
    "Old Site B-Side Cassette",
    "Celestial Resort B-Side Cassette",
    "Golden Ridge B-Side Cassette",
    "Mirror Temple B-Side Cassette",
    "Reflections B-Side Cassette",
    "Summit B-Side Cassette"
}

heart_locations = {
    "Pointless Machine",
    "Resurrections",
    "Scattered And Lost",
    "Eye Of The Storm",
    "Quiet And Falling",
    "Heavy And Frail",
    "Pink Sunrise"
}