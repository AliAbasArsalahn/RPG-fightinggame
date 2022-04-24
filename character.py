# Projekt: RPG-fightinggame | Modul: character
# Author: Ali Abas Arsalahn
# Datum: 21.04.2022

from abc import ABC, abstractmethod
from random import randrange

# from attr import attr


class Character(ABC):

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
        pass

    def __str__(self) -> str:
        pass

    @property
    def level(self) -> int:
        return self.level

    @level.setter
    def level(self, value: int) -> None:
        self.level += value

    @property
    def experience(self) -> int:
        return self.experience

    @experience.setter
    def experience(self, value) -> None:
        self.experience += value

    def level_up(self, experience: int) -> None:
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
        return self.current_health

    @current_health.setter
    def current_health(self, damage) -> None:
        self.current_health -= damage

    @abstractmethod
    def speak() -> str:
        pass

    def roll_dice(max_range) -> int:
        return randrange(1, max_range)

    @property
    def dodge_chance(self) -> float:
        return self.dodge_chance

    @dodge_chance.setter
    def dodge_chance(self) -> None:
        self.dodge_chance = 0.01 * self.attributes["agility"]
