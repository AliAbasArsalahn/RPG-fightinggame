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

    def combat(player: Character, npc: Character) -> None:
        """Combat function."""
        # player.interactions.
        both_combatants_alive = True
        if player.attributes.health >= 0 or npc.attributes.health >= 0:
            both_combatants_alive = False
        while both_combatants_alive:
            if player.attributes.health >= 0 or npc.attributes.health >= 0:
                both_combatants_alive = False

    def speak() -> None:
        pass
