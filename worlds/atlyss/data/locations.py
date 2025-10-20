import typing


class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str

all_locations = {
    "A Warm Welcome": LocationData(1, "Sanctum"),
    "Communing Catacombs": LocationData(2, "Sanctum"),
    "Diva Must Die": LocationData(3, "Sanctum"),
    "The Keep Within": LocationData(4, "Sanctum"),
    "Tethering Grove": LocationData(5, "Sanctum"),
    "The Gylyphik Booklet": LocationData(6, "Sanctum"),
    "Wicked Wizboars": LocationData(7, "Sanctum"),
    "Nulversa Magica": LocationData(8, "Sanctum"),
    "Cold Shoulder": LocationData(9, "Sanctum"),
    "Mastery of Mind": LocationData(10, "Sanctum"),
    "Blossom of Life": LocationData(11, "Sanctum"),
    "Sanctum Catacombs (1-6): Complete": LocationData(1001, "Sanctum Catacombs"),
    "Sanctum Catacombs (6-12): Complete": LocationData(1002, "Sanctum Catacombs"),
    "Sanctum Catacombs (12-18): Complete": LocationData(1003, "Sanctum Catacombs"),
    "Crescent Grove (15-20): Complete": LocationData(1004, "Crescent Grove"),
    "Crescent Grove (20-25): Complete": LocationData(1005, "Crescent Grove"),
    "Angela: Slap Ass": LocationData(2001, "Sanctum"),
    "Sanctum: Chest at Top of Tower": LocationData(2002, "Sanctum"),
    "Sanctum: Chest Behind Barracks": LocationData(2003, "Sanctum"),
    "Sanctum: Chest Inside Hill": LocationData(2004, "Sanctum"),
}