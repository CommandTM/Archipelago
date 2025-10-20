from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
if TYPE_CHECKING:
    from .world import AtlyssWorld
from worlds.atlyss.data.locations import all_locations

class AtlyssLocation(Location):
    game = "Atlyss"

location_name_to_id = {name: data.id for name, data in all_locations.items()}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations[location_name] for location_name in location_names}

def create_all_locations(world: AtlyssWorld) -> None:
    for location_name in all_locations:
        location_data = all_locations[location_name]

        location = AtlyssLocation(world.player, location_name, location_data.id, world.get_region(location_data.region))

        world.get_region(location_data.region).locations.append(location)

