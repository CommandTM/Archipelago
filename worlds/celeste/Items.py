from BaseClasses import Item, ItemClassification
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any

class CelesteItem(Item):
    game: str = "Celeste"

item_table = {
    "Strawberry": ItemData(69000000, ItemClassification.progression),
    "Cassette": ItemData(69000001, ItemClassification.filler),
    "Crystal Heart": ItemData(69000002, ItemClassification.filler),
    "Nothing": ItemData(69000003, ItemClassification.filler),
    "Something": ItemData(69000004, ItemClassification.filler)
}

item_frequencies = {
    "Strawberry": 170,
    "Cassette": 7,
    "Crystal Heart": 7,
    "Nothing": 5,
    "Something": 1
}