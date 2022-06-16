"""Character modul. Includes the abstract class character and it's methods"""


from interactions import Interactions
from attributes import Attributes
from names import Name
from race import Race


class Character():
    """
    properties: name: str, race: str, attributes: dict, level: int, experience: int
    max_health: int, current_health: int, dodge_chance: float
    """

    def __init__(self) -> None:
        """
        Character Creation.
        """
        self.name = Name()
        self.race = Race()
        self.attributes = Attributes()
        self.interactions = Interactions()
        self.spells = {}

    def __repr__(self) -> str:
        """repr method"""
        pass

    def __str__(self) -> str:
        """str method"""
        pass

    def move(self) -> None:
        pass
