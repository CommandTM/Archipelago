import typing
from Options import Choice, Option, Toggle, Range

class OldSiteCost(Range):
    """How many strawberries it would take to unlock Old Site"""
    display_name = "Old Site Cost"
    default = 10
    range_start = 1
    range_end = 20

class CelestialResortCost(Range):
    """How many strawberries it would take to unlock Celstial Resort"""
    display_name = "Celestial Resort Cost"
    default = 30
    range_start = 5
    range_end = 38

class GoldenRidgeCost(Range):
    """How many strawberries it would take to unlock Golden Ridge"""
    display_name = "Golden Ridge Cost"
    default = 50
    range_start = 10
    range_end = 63

class MirrorTempleCost(Range):
    """How many strawberries it would take to unlock Mirror Temple"""
    display_name = "Mirror Temple Cost"
    default = 70
    range_start = 15
    range_end = 92

class ResurectionsCost(Range):
    """How many strawberries it would take to unlock Resurections"""
    display_name = "Resurections Cost"
    default = 90
    range_start = 20
    range_end = 123

class SummitCost(Range):
    """How many strawberries it would take to unlock Summit"""
    display_name = "Summit Cost"
    default = 110
    range_start = 25
    range_end = 123

class CassetteRandomize(Toggle):
    """Should B-Side Cassettes be randomized"""
    display_name = "Exclude B-Side Cassettes"
    default = 0

class CrystalHeartsRandomize(Toggle):
    """Should Crystal Hearts be randomized"""
    display_name = "Exclude Crystal Hearts"
    default = 0

class JewelsRandomize(Toggle):
    """Should the Jewels in 7a be randomized"""
    display_name = "Exclude 7a Jewels"
    default = 0

celeste_options: typing.Dict[str, type(Option)] = {
    "old_site_cost": OldSiteCost,
    "celestial_resort_cost": CelestialResortCost,
    "golden_ridge_cost": GoldenRidgeCost,
    "mirror_temple_cost": MirrorTempleCost,
    "resurections_cost": ResurectionsCost,
    "summit_cost": SummitCost,
    "cassettes_random": CassetteRandomize,
    "crystal_heart_random": CrystalHeartsRandomize,
    "jewel_random": JewelsRandomize,
}
