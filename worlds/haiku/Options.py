from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Choice, PerGameCommonOptions



#class goal(Choice):
#    """What should the goal of your game be?"""
#    display_name = "Goal"
#    option_virus = 0
#    option_true = 1


class darkRoomLogic(DefaultOnToggle):
    """Should dark rooms logically require Bulblet?"""
    display_name = "Dark Room Logic"


#class shuffleMapDisruptors(DefaultOnToggle):
#    """Should Map Disruptors be randomized?"""
#    display_name = "Shuffle Map Disruptors"


#class shuffleTrainStations(DefaultOnToggle):
#    """Should Train Stations be randomized?"""
#    display_name = "Shuffle Train Stations"


#class shuffleCreators(DefaultOnToggle):
#    """Should Creators be randomized?"""
#    display_name = "Shuffle Creators"


class shuffleWrench(DefaultOnToggle):
    """Should the Wrench be randomized?"""
    display_name = "Shuffle Wrench"


class shuffleChipSockets(DefaultOnToggle):
    """Should Chip Sockets be randomized?"""
    display_name = "Shuffle Chip Sockets"


#class deathLink(Toggle):
#    """When you die, everyone dies. Of course the reverse is true too."""
#    display_name = "Death Link"


@dataclass
class HaikuOptions(PerGameCommonOptions):
    # ending: goal
    # dark_room_logic: darkRoomLogic
    # map_disruptors: shuffleMapDisruptors
    # train_stations: shuffleTrainStations
    # creators: shuffleCreators
    wrench: shuffleWrench
    chip_sockets: shuffleChipSockets
    # death_link: deathLink
