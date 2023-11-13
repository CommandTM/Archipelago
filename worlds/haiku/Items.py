from BaseClasses import Item, ItemClassification
from .data import ItemDict
import typing


class HaikuItem(Item):
    game: str = "Haiku The Robot"


def createItems(self):
    offset = 901403403
    itempool = []
    for name, type in ItemDict.abilites:
        itempool += createItem(name, type, offset)
        offset += 1
        break
    self.multiworld.itempool += itempool


def createItem(self, name: str, classification: ItemClassification, itemCode: int) -> Item:
    item = HaikuItem(name, classification, itemCode, self.player)
    return item