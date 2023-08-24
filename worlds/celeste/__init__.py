from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

class CelesteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to making a computer play Celeste that just so happens to have Archipelago combatibility.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Probably Command"]
    )]