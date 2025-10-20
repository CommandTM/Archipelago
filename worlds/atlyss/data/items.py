import typing

from BaseClasses import ItemClassification

class ItemData(typing.NamedTuple):
    id: typing.Optional[int]
    classification: any

all_items = {
    "Outer Sanctum Portal": ItemData(1, ItemClassification.progression),
    "Arcwood Pass Portal": ItemData(2, ItemClassification.progression),
    "Effold Terrace Portal": ItemData(3, ItemClassification.progression),
    "Tuul Valley Portal": ItemData(4, ItemClassification.progression),
    "Crescent Road Portal": ItemData(5, ItemClassification.progression),
    "Crescent Keep Portal": ItemData(6, ItemClassification.progression),
    "Crescent Grove Portal": ItemData(7, ItemClassification.progression),
    "Gate of the Moon Portal": ItemData(8, ItemClassification.progression),
    "Luvora Garden Portal": ItemData(9, ItemClassification.progression),
    "Wall of the Stars Portal": ItemData(10, ItemClassification.progression),
    "Trial of the Stars Portal": ItemData(11, ItemClassification.progression),
    "Tuul Enclave Portal": ItemData(12, ItemClassification.progression),
    "Bularr Fortress Portal": ItemData(13, ItemClassification.progression),
    "Sanctum Catacombs (1-6) Unlock": ItemData(1001, ItemClassification.progression),
    "Sanctum Catacombs (6-12) Unlock": ItemData(1002, ItemClassification.progression),
    "Sanctum Catacombs (12-18) Unlock": ItemData(1003, ItemClassification.progression),
    "Crescent Grove (15-20) Unlock": ItemData(1004, ItemClassification.progression),
    "Crescent Grove (20-25) Unlock": ItemData(1005, ItemClassification.progression),
    "Tome of Lesser Experience": ItemData(2001, ItemClassification.filler),
    "Tome of Experience": ItemData(2002, ItemClassification.filler),
    "Tome of Greater Experience": ItemData(2003, ItemClassification.filler),
}