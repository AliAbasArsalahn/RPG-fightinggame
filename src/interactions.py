"""This module hosts interactions between character objects"""

from random import randrange


class Interactions:
    """
    Interactions class. Contains generic Methods, that characters can use.
    Methods: roll_dice, combat, speak
    """
    def roll_dice(max_range: int) -> int:
        """
        Takes an int as argument, increments it by one and returns a random number,
        that is between the given number and 1.
        """
        return randrange(1, max_range + 1)

    # incomplete
    def combat(object_1: object, object_2: object) -> None:
        """Combat function."""
        both_combatants_alive = True
        while both_combatants_alive:
            pass

    def speak() -> None:
        pass
