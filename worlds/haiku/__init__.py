from typing import Dict, Any

from BaseClasses import Item, Region, Entrance, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import fillItemTable, item_table, HaikuItem
from .data.ItemDict import necessaryItems, chipSockets, junkWeights
from .data.LocationDict import exclusionTable
from .data.Presets import optionsPresets
from .Locations import advancement_table, fillAdvancementTable, HaikuAdvancement
from .Options import HaikuOptions
from .Regions import linkHaikuAreas, haikuRegions
from .Rules import setRules, setCompletionRules

offset = 1651104000


class HaikuWebWorld(WebWorld):
    theme = "dirt"
    options_presets = optionsPresets
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up Haiku, The Robot for a Multiworld game.",
        "English",
        "setup_en.md",
        "setup/en",
        ["CommandTM"]
    )]


class HaikuWorld(World):
    """
    [PLACEHOLDER, LAUREN PLEASE NAME]
    """
    game = "Haiku, The Robot"
    web = HaikuWebWorld()
    data_version = 1
    options_dataclass = HaikuOptions
    options: HaikuOptions

    fillItemTable(offset)
    fillAdvancementTable(offset)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    def create_items(self):
        itempool = []
        exculsionPool = set()

        for name, num in necessaryItems.items():  # Required Items
            itempool += [name] * num

        # region Options
        if self.options.wrench.value:  # Wrench Option
            itempool += ["Adjustable Wrench"]
        else:
            exculsionPool.update(exclusionTable["wrench"])

        #if self.options.map_disruptors.value:  # Map Disruptors Option
        #    for name, num in mapDisruptors.items():
        #        itempool += [name] * num
        #else:
        #    exculsionPool.update(exclusionTable["mapDisruptors"])

        #if self.options.train_stations.value:  # Train Stations Option
        #    for name, num in trainStations.items():
        #        itempool += [name] * num
        #else:
        #    exculsionPool.update(exclusionTable["trainStations"])

        if self.options.chip_sockets.value:  # Chip Sockets Option
            for name, num in chipSockets.items():
                itempool += [name] * num
        else:
            exculsionPool.update(exclusionTable["chipSockets"])

        #if self.options.creators.value:  # Creators Option
        #    for name, num in creators.items():
        #        itempool += [name] * num
        #else:
        #    exculsionPool.update(exclusionTable["creators"])
        # endregion

        itempool += self.multiworld.random.choices(list(junkWeights.keys()), list(junkWeights.values()),
                                                   k=len(self.location_names) - len(itempool) - len(exculsionPool))

        # Converts itempool to actual items, then adds them to the Multiworld's itempool
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool

    def create_regions(self):
        def HaikuRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations += [HaikuAdvancement(self.player, loc_name, loc_data.id, ret)
                              for loc_name, loc_data in advancement_table.items()
                              if loc_data.region == region_name and
                              (loc_name not in exclusionTable["wrench"] or self.options.wrench.value) and
                              #(loc_name not in exclusionTable["mapDisruptors"] or self.options.map_disruptors.value) and
                              #(loc_name not in exclusionTable["trainStations"] or self.options.train_stations.value) and
                              (loc_name not in exclusionTable["chipSockets"] or self.options.chip_sockets.value)] #and
                              #(loc_name not in exclusionTable["creators"] or self.options.creators.value)]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [HaikuRegion(*r) for r in haikuRegions]
        linkHaikuAreas(self.multiworld, self.player)

    def set_rules(self):
        setRules(self, self.multiworld, self.player)
        setCompletionRules(self, self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = HaikuItem(name, item_data.classification, item_data.code, self.player)
        return item

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict("wrench", "chip_sockets")
        slot_data["baseID"] = offset
        return slot_data
