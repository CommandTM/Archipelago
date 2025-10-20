from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import AtlyssWorld
from worlds.generic.Rules import set_rule


def set_all_rules(world: AtlyssWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: AtlyssWorld) -> None:
    set_rule(world.get_entrance("Sanctum_Outer Sanctum"),
             lambda state: state.has("Outer Sanctum Portal", world.player))

    set_rule(world.get_entrance("Outer Sanctum_Arcwood Pass"),
             lambda state: state.has("Arcwood Pass Portal", world.player))

    set_rule(world.get_entrance("Outer Sanctum_Effold Terrace"),
             lambda state: state.has("Effold Terrace Portal", world.player))

    set_rule(world.get_entrance("Outer Sanctum_Tuul Valley"),
             lambda state: state.has("Tuul Valley Portal", world.player))

    set_rule(world.get_entrance("Arcwood Pass_Crescent Road"),
             lambda state: state.has("Crescent Road Portal", world.player))

    set_rule(world.get_entrance("Tuul Valley_Tuul Enclave"),
             lambda state: state.has("Tuul Enclave Portal", world.player))

    set_rule(world.get_entrance("Crescent Road_Luvora Garden"),
             lambda state: state.has("Luvora Garden Portal", world.player))

    set_rule(world.get_entrance("Crescent Road_Crescent Keep"),
             lambda state: state.has("Crescent Keep Portal", world.player))

    set_rule(world.get_entrance("Crescent Keep_Crescent Grove"),
             lambda state: state.has("Crescent Grove Portal", world.player))

    set_rule(world.get_entrance("Crescent Keep_Gate of the Moon"),
             lambda state: state.has("Gate of the Moon Portal", world.player))

    set_rule(world.get_entrance("Gate of the Moon_Wall of the Stars"),
             lambda state: state.has("Wall of the Stars Portal", world.player))

    set_rule(world.get_entrance("Wall of the Stars_Trial of the Stars"),
             lambda state: state.has("Trial of the Stars Portal", world.player))

    set_rule(world.get_entrance("Tuul Enclave_Bularr Fortress"),
             lambda state: state.has("Bularr Fortress Portal", world.player))

def set_all_location_rules(world: AtlyssWorld) -> None:
    set_rule(world.get_location("Communing Catacombs"),
             lambda state: state.can_reach("Sanctum Catacombs", "Region", world.player) and
                            state.has("Sanctum Catacombs (1-6) Unlock", world.player) and
                            state.can_reach("A Warm Welcome", "Location", world.player))

    set_rule(world.get_location("Diva Must Die"),
             lambda state: state.can_reach("Effold Terrace", "Region", world.player) and
                            state.can_reach("Communing Catacombs", "Location", world.player))

    set_rule(world.get_location("The Keep Within"),
             lambda state: state.can_reach("Crescent Keep", "Region", world.player) and
                            state.can_reach("Diva Must Die", "Location", world.player))

    set_rule(world.get_location("Tethering Grove"),
             lambda state: state.can_reach("Crescent Grove", "Region", world.player) and
                            state.has("Crescent Grove (15-20) Unlock", world.player) and
                            state.can_reach("The Keep Within", "Location", world.player))

    set_rule(world.get_location("The Gylyphik Booklet"),
             lambda state: state.can_reach("Luvora Garden", "Region", world.player) and
                            state.can_reach("Tuul Enclave", "Region", world.player) and
                            state.can_reach("Crescent Grove", "Region", world.player) and
                            state.has("Crescent Grove (20-25) Unlock", world.player) and
                            state.can_reach("Bularr Fortress", "Region", world.player))

    set_rule(world.get_location("Wicked Wizboars"),
             lambda state: state.can_reach("Tuul Valley", "Region", world.player))

    set_rule(world.get_location("Nulversa Magica"),
             lambda state: state.can_reach("Crescent Grove", "Region", world.player) and
                            state.has("Crescent Grove (20-25) Unlock", world.player) and
                            state.can_reach("Tuul Enclave", "Region", world.player))

    set_rule(world.get_location("Sanctum Catacombs (1-6): Complete"),
             lambda state: state.can_reach("Sanctum Catacombs", "Region", world.player) and
                           state.has("Sanctum Catacombs (1-6) Unlock", world.player))

    set_rule(world.get_location("Sanctum Catacombs (6-12): Complete"),
             lambda state: state.can_reach("Sanctum Catacombs", "Region", world.player) and
                           state.has("Sanctum Catacombs (6-12) Unlock", world.player))

    set_rule(world.get_location("Sanctum Catacombs (12-18): Complete"),
             lambda state: state.can_reach("Sanctum Catacombs", "Region", world.player) and
                           state.has("Sanctum Catacombs (12-18) Unlock", world.player))

    set_rule(world.get_location("Crescent Grove (15-20): Complete"),
             lambda state: state.can_reach("Crescent Grove", "Region", world.player) and
                           state.has("Crescent Grove (15-20) Unlock", world.player))

    set_rule(world.get_location("Crescent Grove (20-25): Complete"),
             lambda state: state.can_reach("Crescent Grove", "Region", world.player) and
                           state.has("Crescent Grove (20-25) Unlock", world.player))



def set_completion_condition(world: AtlyssWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: (state.can_reach("Crescent Grove", "Region", world.player) and
                                                                        state.has("Crescent Grove (20-25) Unlock", world.player))