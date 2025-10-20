from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle


class CraftingQuests(Toggle):
    """
    Should crafting quests be included in randomization?
    """
    display_name = "Include Crafting Quests"

@dataclass
class AtlyssOptions(PerGameCommonOptions):
    crafting_quests: CraftingQuests