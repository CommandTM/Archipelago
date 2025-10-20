from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


class AtlyssWebWorld(WebWorld):
    game = "Atylss"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Atylss for Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["CommandTM"]
    )

    tutorials = [setup_en]

    # TODO: Implement Later
    #option_groups =
    #options_presets =