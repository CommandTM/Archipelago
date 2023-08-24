from BaseClasses import MultiWorld


def link_celeste_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))
        

# (Region name, list of exits)
celeste_regions = [
    ("Menu", ["City Entrance"]),
    ("Forsaken City", ["Site Entrance"]),
    ("Old Site", ["Resort Entrance"]),
    ("Celestial Resort", ["Ridge Entrance"]),
    ("Golden Ridge", ["Temple Entrance"]),
    ("Mirror Temple", ["Reflect Entrance"]),
    ("Reflections", ["Summit Entrance"]),
    ("Summit", []),
]


# (Entrance, region pointed to)
mandatory_connections = [
    ("City Entrance", "Forsaken City"),
    ("Site Entrance", "Old Site"),
    ("Resort Entrance", "Celestial Resort"),
    ("Ridge Entrance", "Golden Ridge"),
    ("Temple Entrance", "Mirror Temple"),
    ("Reflect Entrance", "Reflections"),
    ("Summit Entrance", "Summit")
]