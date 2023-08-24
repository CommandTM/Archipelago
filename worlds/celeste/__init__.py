from typing import Dict, Any, Iterable, Optional, Union
from BaseClasses import Tutorial, Item, Region, Entrance
from worlds.AutoWorld import World, WebWorld
from .Items import CelesteItem, item_table, ItemData, create_items
from .Locations import advancement_table, exclusion_table, CelesteAdvancement
from .Options import Celeste_options, CelesteOptions, fetch_options
from .Rules import set_rules
from .Regions import create_regions, celeste_regions, link_celeste_areas
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

    def create_items(self):
        itempool = []
        itempool += ["Strawberry"]
        if self.multiworld.cassettes_random[self.player] == 1:
            itempool += ["Cassette"]
        if self.multiworld.crystal_heart_random[self.player] == 1:
            itempool += ["Crystal Heart"]
        if self.multiworld.jewel_random[self.player] == 1:
            itempool += ["Nothing"]
            itempool += ["Something"]
        exclusion_pool = set()
        if not self.multiworld.cassettes_random[self.player]:
            exclusion_pool.update(exclusion_table["Cassettes"])
        if not self.multiworld.crystal_heart_random[self.player]:
            exclusion_pool.update(exclusion_table["Crystal Hearts"])
        if not self.multiworld.jewel_random[self.player]:
            exclusion_pool.update(exclusion_table["7a Jewels"])

        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool
    
    def set_rules(self):
        set_rules(self.multiworld, self.player)
    
    def create_regions(self):
        def CelesteRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations = [CelesteAdvancement(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in advancement_table.items()
                             if loc_data.region == region_name and
                                loc_name not in exclusion_table["Cassettes"] and
                                loc_name not in exclusion_table["Crystal Hearts"] and
                                loc_name not in exclusion_table["7a Jewels"]]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret
        
        self.multiworld.regions += [CelesteRegion(*r) for r in celeste_regions]
        link_celeste_areas(self.multiworld, self.player)

    def fill_slot_data(self):
        return {
            "old_site_cost": self.multiworld.old_site_cost[self.player].value,
            "celestial_resort_cost": self.multiworld.celestial_resort_cost[self.player].value,
            "golden_ridge_cost": self.multiworld.golden_ridge_cost[self.player].value,
            "mirror_temple_cost": self.multiworld.mirror_temple_cost[self.player].value,
            "resurections_cost": self.multiworld.resurections_cost[self.player].value,
            "summit_cost": self.multiworld.summit_cost[self.player].value,
            "cassettes_random": self.multiworld.cassettes_random[self.player].value,
            "crystal_heart_random": self.multiworld.crystal_heart_random[self.player].value,
            "jewel_random": self.multiworld.jewel_random[self.player].value,
        }
    
    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = CelesteItem(name, item_data.classification, item_data.code, self.player)
        return item