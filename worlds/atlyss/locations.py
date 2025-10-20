from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
if TYPE_CHECKING:
    from .world import AtlyssWorld
from worlds.atlyss.data.locations import all_locations, always_locations, crafting_quests, skill_quests

class AtlyssLocation(Location):
    game = "Atlyss"

location_name_to_id = {name: data.id for name, data in all_locations.items()}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations[location_name] for location_name in location_names}

def create_all_locations(world: AtlyssWorld) -> None:
    create_locations_from_list(world, always_locations)

    if world.options.crafting_quests:
        create_locations_from_list(world, crafting_quests)

    if world.options.skill_quests:
        create_locations_from_list(world, skill_quests)


def create_locations_from_list(world: AtlyssWorld, location_list: list[str]) -> None:
    for location_name in location_list:
        location_data = all_locations[location_name]

        location = AtlyssLocation(world.player, location_name, location_data.id, world.get_region(location_data.region))

        world.get_region(location_data.region).locations.append(location)

