from BaseClasses import Item, ItemClassification
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any

class CelesteItem(Item):
    game: str = "Celeste"

item_table = {
    "Starwberry": ItemData(69000000, ItemClassification.progression)
}

item_frequencies = {
    "Starwberry": 170,
}