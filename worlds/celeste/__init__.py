from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

class CelesteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Celeste game on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Probably Command"]
    )]