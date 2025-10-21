from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, Range


class CraftingQuests(Toggle):
    """
    Should crafting quests be included in randomization?
    E.G. Angela: The Gylyphik Booklet
    """
    display_name = "Include Crafting Quests"
    default = True


class SkillQuests(Toggle):
    """
    Should skill quests be included in randomization?
    E.G. Angela: Cold Shoulder
    """
    display_name = "Include Skill Quests"
    default = False


class EarlyArcwood(Toggle):
    """
    Should the Arcwood Pass Portal be placed early in the multiworld?
    """
    display_name = "Early Arcwood Pass"
    default = True


class ExpMult(Range):
    """
    Multiplier for gained Exp
    """
    display_name = "Experience Multiplier"
    range_start = 1
    range_end = 5
    default = 3


@dataclass
class AtlyssOptions(PerGameCommonOptions):
    crafting_quests: CraftingQuests
    skill_quests: SkillQuests
    early_arcwood: EarlyArcwood
    exp_mult: ExpMult