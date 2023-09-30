from BaseClasses import Tutorial, Item, Region, Entrance
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import exclusion_rules
from .Items import CelesteItem, item_table, item_frequencies
from .Locations import CelesteAdvancement, advancement_table, tape_locations, heart_locations
from .Options import celeste_options
from .Rules import set_rules
from .Regions import celeste_regions, link_celeste_areas

class CelesteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to making a computer play Celeste that just so happens to have Archipelago compatibility.",
        "English",
        "setup_en.md",
        "setup/en",
        ["CommandTM"]
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
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    data_version = 2

    option_definitions = celeste_options

    def create_items(self):
        exclusion_pool = set()
        if self.multiworld.cassettes_random[self.player] == 1:
            exclusion_pool.update(tape_locations)
        if self.multiworld.crystal_heart_random[self.player] == 1:
            exclusion_pool.update(heart_locations)
        exclusion_rules(self.multiworld, self.player, exclusion_pool)
        
        itempool = []
        itempool += ["Strawberry"] * item_frequencies["Strawberry"]
        if self.multiworld.cassettes_random[self.player] == 0:
            itempool += ["Cassette"] * item_frequencies["Cassette"]
        else:
            itempool += ["Nothing"] * item_frequencies["Cassette"]
        if self.multiworld.crystal_heart_random[self.player] == 0:
            itempool += ["Crystal Heart"] * item_frequencies["Crystal Heart"]
        else:
            itempool += ["Nothing"] * item_frequencies["Crystal Heart"]

        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool
    
    def set_rules(self):
        set_rules(self.multiworld, self.player)
    
    def create_regions(self):
        def CelesteRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations = [CelesteAdvancement(self.player, loc_name, loc_data.id, ret)
                            for loc_name, loc_data in advancement_table.items()
                            if loc_data.region == region_name]
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
            "crystal_heart_random": self.multiworld.crystal_heart_random[self.player].value
        }
    
    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = CelesteItem(name, item_data.classification, item_data.code, self.player)
        return item
