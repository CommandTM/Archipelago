from .Items import CelesteItem, item_table, item_frequencies
from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule

class CelesteWeb(WebWorld):
    theme = "ice"
    tutorials: [
        Tutorial(
            tutorial_name = "Multiworld Setup Tutorial",
            description = "Not Quite There Yet",
            language = "English",
            authors = "No One"
        )
    ]

class CelesteWorld(World):
    """This Isn't Going To Go Well Is It?"""
    game = "Celeste",
    data_version = 6
    web = CelesteWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
