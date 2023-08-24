from worlds.generic.Rules import set_rule
from BaseClasses import MultiWorld

def set_rules(multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_entrance("Site Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.old_site_cost[player])))
    set_rule(multiworld.get_entrance("Resort Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.celestial_resort_cost[player])))
    set_rule(multiworld.get_entrance("Ridge Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.golden_ridge_cost[player])))
    set_rule(multiworld.get_entrance("Temple Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.mirror_temple_cost[player])))
    set_rule(multiworld.get_entrance("Reflect Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.reflections_cost[player])))
    set_rule(multiworld.get_entrance("Summit Entrance", player),
        lambda state: (state.has("Strawberry", player, state.multiworld.summit_cost[player])))