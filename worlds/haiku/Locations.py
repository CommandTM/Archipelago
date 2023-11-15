from BaseClasses import Location
from .data import LocationDict
import typing


class AdvData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class HaikuAdvancement(Location):
    game: str = "Haiku"


advancement_table = {}


def fillAdvancementTable(offset):
    for name in LocationDict.all_locations:
        advancement_table[name] = AdvData(offset, LocationDict.all_locations[name])
        offset += 1
