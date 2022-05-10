# Projekt: RPG-fightinggame | Modul: character
# Author: Ali Abas Arsalahn
# Datum: 21.04.2022
"""Character modul. Includes the abstract class character and it's methods"""


from abc import ABC, abstractmethod
from random import randrange

# from attr import attr


class Character(ABC):
    """
    Abstract Class Character. Interface for building playable character classes.
    Methods: level_up, speak, roll_dice
    properties: name: str, race: str, attributes: dict, level: int, experience: int
    max_health: int, current_health: int, dodge_chance: float
    """
    def __init__(self, name: str, race: str) -> object:
        self.name: str = name
        self.race: str = race
        self.inventory: list = []
        self.attributes = {
            "strength": 0,
            "intellect": 0,
            "agility": 0,
            "stamina": 0
        }

    def __repr__(self) -> str:
        """must be implemented by every subclass"""
        return f"{self.name}, {self.race}"

    def __str__(self) -> str:
        """must be implemented by every subclass"""
        return f"Character name: {self.name}, race: {self.race}"

    @property
    def level(self) -> int:
        """Level getter."""
        return self.level

    @level.setter
    def level(self, value: int) -> None:
        """Level setter"""
        self.level += value

    @property
    def experience(self) -> int:
        """experience getter"""
        return self.experience

    @experience.setter
    def experience(self, value) -> None:
        """Experience setter. Get's called after every combat."""
        self.experience += value

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
        max_health = self.attributes["stamina"] * 10

    @property
    def current_health(self) -> int:
        """Returns current health"""
        return self.current_health

    @current_health.setter
    def current_health(self, damage) -> None:
        """decreases health if damage is sustained. Get's called during combat
        on every enemy attack."""
        self.current_health -= damage

    @abstractmethod
    def speak(self) -> tuple: # no application planned yet
        """checks intelligence attributes and allows speach acording to the stat."""
        intelligence = self.attributes.get("intelligence")
        if intelligence > 3:
            can_speak_to_peasants = True
        if intelligence > 5:
            can_speak_to_citizens = True
        if intelligence > 8:
            can_speak_to_nobles = True

        speech = (can_speak_to_peasants, can_speak_to_citizens, can_speak_to_nobles)
        return speech

    def roll_dice(max_range: int) -> int: # might implement in a seperate modul
        """returns a random number. Is used to determine damage value of
        every ability."""
        return randrange(1, max_range)

    @property
    def dodge_chance(self) -> float:
        """dodge_chance getter"""
        return self.dodge_chance

    @dodge_chance.setter
    def dodge_chance(self) -> None:
        """Dodge_chance get's set to 0.01% for each point of agility a character has."""
        self.dodge_chance = 0.01 * self.attributes["agility"]
