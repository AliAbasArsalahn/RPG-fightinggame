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
        self._inventory: list = []
        self.attributes: object = Attributes()
        self.interactions: object = Interactions()

    def __repr__(self) -> str:
        """must be implemented by every subclass"""
        return f"{self._name}, {self._race}"

    def __str__(self) -> str:
        """must be implemented by every subclass"""
        return f"Character name: {self._name}, race: {self._race}"

    def move(self) -> None:
        pass
    # @property
    # def dodge_chance(self) -> float:
    #     """dodge_chance getter"""
    #     return self.dodge_chance

    # @dodge_chance.setter
    # def dodge_chance(self) -> None:
    #     """dodge_chance setter"""
    #     self.dodge_chance = 0.01 * self._attributes["agility"]
