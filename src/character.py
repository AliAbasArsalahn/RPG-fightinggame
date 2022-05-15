"""Character modul. Includes the abstract class character and it's methods"""


from interactions import Interactions
from attributes import Attributes
from names import Name


class Character():
    """
    properties: name: str, race: str, attributes: dict, level: int, experience: int
    max_health: int, current_health: int, dodge_chance: float
    """

    def __init__(self) -> None:
        """
        Character Creation.
        Required Arguments: Name, Race
        """
        self.name = Name
        self.race = None
        # self._inventory: list = []
        self.attributes = Attributes()
        self.interactions = Interactions

    def __repr__(self) -> str:
        """repr method"""
        pass

    def __str__(self) -> str:
        """str method"""
        pass

    @property
    def race(self) -> str:
        return self._race

    @race.setter
    def race(self, racepick: str) -> None:
        AVAILABLE_RACES = ['Human', 'Dwarf', 'Elf']
        if racepick in AVAILABLE_RACES:
            self._race = racepick

    def move(self) -> None:
        pass
