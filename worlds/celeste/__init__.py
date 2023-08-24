from typing import Dict, Any, Iterable, Optional, Union
from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from .Items import CelesteItem, item_table, ItemData, create_items
from .Locations import advancement_table, CelesteLocation
from .Options import Celeste_options, CelesteOptions, fetch_options
from .Rules import set_rules
from .Regions import create_regions
from . import Options

class CelesteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to making a computer play Celeste that just so happens to have Archipelago combatibility.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Probably Starlord"]
    )]
    theme="ice"

class CelesteWorld(World):
    """
    Now, this is a story all about how
    My life got flipped-turned upside down
    And I'd like to take a minute
    Just sit right there
    I'll tell you how I became a climber of a mountain called Celeste
    """
    game = "Celeste"
    topology_present = False
    web = CelesteWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = advancement_table

    data_version = 1

    option_definitions = Celeste_options