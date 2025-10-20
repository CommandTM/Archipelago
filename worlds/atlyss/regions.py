from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from worlds.atlyss.data.regions import all_regions
from worlds.stardew_valley.strings.entrance_names import Entrance

if TYPE_CHECKING:
    from .world import AtlyssWorld


def create_and_connect_regions(world: AtlyssWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: AtlyssWorld) -> None:
    regions = []

    for region_name in all_regions:
        region = Region(region_name, world.player, world.multiworld)
        regions.append(region)

    world.multiworld.regions += regions

def connect_regions(world: AtlyssWorld) -> None:
    for region_name in all_regions:
        connections = all_regions[region_name]
        region = world.get_region(region_name)

        for connection_name in connections:
            name = f"{region_name}_{connection_name}"
            region.connect(world.get_region(connection_name), name)