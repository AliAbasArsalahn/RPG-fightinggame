"""Character modul. Includes the abstract class character and it's methods"""


from interactions import Interactions
from attributes import Attributes


class Character():
    """
    properties: name: str, race: str, attributes: dict, level: int, experience: int
    max_health: int, current_health: int, dodge_chance: float
    """

    def __init__(self, name: str, race: str) -> object:
        """
        Character Creation.
        Required Arguments: Name, Race
        """
        self._name: str = name
        self._race: str = race
        # self._inventory: list = []
        self.attributes: object = Attributes
        self.interactions: object = Interactions

    def __repr__(self) -> str:
        """repr method"""
        return f"{self._name}, {self._race}"

    def __str__(self) -> str:
        """str method"""
        return f"Character name: {self._name}, race: {self._race}"

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
