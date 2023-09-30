from typing import Dict

from BaseClasses import Tutorial
from ..AutoWorld import WebWorld, World

class BK_PicrossWebWord(WebWorld):
    settings_page = "games/Picross/info/en"
    theme = "partyTime"
    tutorials = [
        Tutorial(
            tutorial_name='Setup Guide',
            description='A guide to playing BK Picross',
            language='English',
            file_name='setup_en.md',
            link='setup/en',
            authors=['CommandTM']
        )
    ]

class BK_PicrossWorld(World):
    """
    Play Picross while BKed to gain useful hints
    """
    game = "Picross"
    web = BK_PicrossWebWord()
    data_version = 1

    item_name_to_id: Dict[str, int] = {}
    location_name_to_id: Dict[str, int] = {}

    @classmethod
    def stage_assert_generate(cls, multiworld):
        raise Exception("BK Picross is not generated into worlds, but connects to pre-existing worlds")