from BaseClasses import Item
from worlds.AutoWorld import WebWorld, World
from .Items import fillItemTable, item_table, HaikuItem
from .data.ItemDict import requiredItems, mapDisruptors, trainStations, chipSockets, creators, junkWeights
from .data.LocationDict import exclusionTable
from .Locations import advancement_table, fillAdvancementTable
from .Options import HaikuOptions

offset = 901403403


class HaikuWebWorld(WebWorld):
    theme = "dirt"


class HaikuWorld(World):
    """
    Ah
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

        for name, num in requiredItems.items():  # Required Items
            itempool += [name] * num

        # region Options
        if self.options.wrench:  # Wrench Option
            itempool += ["Adjustable Wrench"]
        else:
            exculsionPool.update(exclusionTable["wrench"])

        if self.options.map_disruptors:  # Map Disruptors Option
            for name, num in mapDisruptors.items():
                itempool += [name] * num
        else:
            exculsionPool.update(exclusionTable["mapDisruptors"])

        if self.options.train_stations:  # Train Stations Option
            for name, num in trainStations.items():
                itempool += [name] * num
        else:
            exculsionPool.update(exclusionTable["trainStations"])

        if self.options.chip_sockets:  # Chip Sockets Option
            for name, num in chipSockets.items():
                itempool += [name] * num
        else:
            exculsionPool.update(exclusionTable["chipSockets"])

        if self.options.creators:  # Creators Option
            for name, num in creators.items():
                itempool += [name] * num
        else:
            exculsionPool.update(exclusionTable["creators"])
        # endregion

        itempool += self.multiworld.random.choices(junkWeights.keys(), junkWeights.values(),
                                                   k=len(self.location_names)-len(itempool)-len(exculsionPool))

        # Converts itempool to actual items, then adds them to the Multiworld's itempool
        itempool = [item for item in map(lambda name: self.create_item(name), itempool)]
        self.multiworld.itempool += itempool

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = HaikuItem(name, item_data.classification, item_data.code, self.player)
        return item
