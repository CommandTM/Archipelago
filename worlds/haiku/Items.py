from BaseClasses import Item, ItemClassification
from .data import ItemDict
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    classification: any


class HaikuItem(Item):
    game: str = "Haiku The Robot"


item_table = {}


def fillItemTable(offset):
    for name in ItemDict.all_items:
        item_table[name] = ItemData(offset, ItemDict.all_items[name])
        offset += 1
