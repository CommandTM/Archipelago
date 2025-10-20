from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .data.items import all_items

if TYPE_CHECKING:
    from .world import AtlyssWorld

class AtlyssItem(Item):
    game = "Atlyss"

item_name_to_id = {name: data.id for name, data in all_items.items()}

def get_random_filler_item_name(world: AtlyssWorld) -> str:
    num = world.random.randint(0, 99)

    if num < 60:
        return "Tome of Lesser Experience"
    elif num < 99:
        return "Tome of Experience"
    else:
        return "Tome of Greater Experience"

def create_item_with_correct_classification(world: AtlyssWorld, name: str) -> AtlyssItem:
    item_data = all_items[name]

    return AtlyssItem(name, item_data.classification, item_data.id, world.player)

def create_all_items(world: AtlyssWorld) -> None:
    itempool = []

    for name in all_items:
        if all_items[name].classification & ItemClassification.progression == ItemClassification.progression:
            itempool.append(create_item_with_correct_classification(world, name))

    if world.options.early_arcwood:
        world.multiworld.early_items[world.player]["Arcwood Pass Portal"] = 1

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

