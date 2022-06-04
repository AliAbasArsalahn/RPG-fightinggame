"""This module hosts interactions between character objects"""

from random import randrange
from character import Character


class Interactions:
    """
    Interactions class. Contains generic Methods, that characters can use.
    Methods: roll_dice, combat, speak
    """
    @staticmethod
    def roll_dice(max_range: int) -> int:
        """
        Takes an int as argument, increments it by one and returns a random number,
        that is between the given number and 1.
        """
        return randrange(1, max_range + 1)

    # incomplete
    def combat(object_1: Character, object_2: Character) -> None:
        """Combat function."""
        object_1.interactions.
        both_combatants_alive = True
        if object_1.attributes.health >= 0 or object_2.attributes.health >= 0:
            both_combatants_alive = False
        while both_combatants_alive:
            if object_1.attributes.health >= 0 or object_2.attributes.health >= 0:
                both_combatants_alive = False

    def speak() -> None:
        pass
