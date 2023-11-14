from worlds.AutoWorld import WebWorld, World
from .Items import fillItemTable, item_table
from .Locations import advancement_table
from .Locations import fillAdvancementTable
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