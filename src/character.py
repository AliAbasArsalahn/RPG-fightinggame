"""Character modul. Includes the abstract class character and it's methods"""


from abc import ABC
from interactions import Interactions


class Character(ABC):
    """
    Abstract Class Character. Interface for building playable character classes.
    Methods: level_up, speak, roll_dice
    properties: name: str, race: str, attributes: dict, level: int, experience: int
    max_health: int, current_health: int, dodge_chance: float
    """

    def __init__(self, name: str, race: str) -> object:
        self._name: str = name
        self._race: str = race
        self._inventory: list = []
        self.interactions = Interactions()
        self._level = None
        self._experience = None
        self._attributes = {
            "strength": 0,
            "intellect": 0,
            "agility": 0,
            "stamina": 0
        }

    def __repr__(self) -> str:
        """must be implemented by every subclass"""
        return f"{self._name}, {self._race}"

    def __str__(self) -> str:
        """must be implemented by every subclass"""
        return f"Character name: {self._name}, race: {self._race}"

    @property
    def level(self) -> int:
        """Level getter."""
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        """Level setter"""
        self._level += value

    @property
    def experience(self) -> int:
        """experience getter"""
        return self._experience

    @experience.setter
    def experience(self, value) -> None:
        """Experience setter. Get's called after every combat."""
        self._experience += value

    def level_up(self, experience: int) -> None:
        """
        Get's called after every combat. Takes experience earned as Argument.
        Increases player level if certain experience tresholds are met.
        """
        pass

    @property
    def max_health(self) -> int:
        """returns self.max_health"""
        return self.max_health

    @max_health.setter
    def max_health(self) -> None:
        """Max health for every character is 10 times stamina"""
        max_health = self._attributes["stamina"] * 10

    @property
    def current_health(self) -> int:
        """Returns current health"""
        return self.current_health

    @current_health.setter
    def current_health(self, damage) -> None:
        """decreases health if damage is sustained. Get's called during combat
        on every enemy attack."""
        self.current_health -= damage

    # def speak(self) -> tuple:
    #     """checks intelligence attributes and allows speach acording to the stat."""
    #     intelligence = self.attributes.get("intelligence")
    #     if intelligence > 3:
    #         can_speak_to_peasants = True
    #     if intelligence > 5:
    #         can_speak_to_citizens = True
    #     if intelligence > 8:
    #         can_speak_to_nobles = True

    #     speech = (can_speak_to_peasants,
    #               can_speak_to_citizens, can_speak_to_nobles)
    #     return speech

    # def roll_dice(max_range: int) -> int:  # might implement in a seperate modul
    #     """returns a random number. Is used to determine damage value of
    #     every ability."""
    #     return randrange(1, max_range)

    @property
    def dodge_chance(self) -> float:
        """dodge_chance getter"""
        return self.dodge_chance

    @dodge_chance.setter
    def dodge_chance(self) -> None:
        """dodge_chance setter"""
        self.dodge_chance = 0.01 * self._attributes["agility"]
