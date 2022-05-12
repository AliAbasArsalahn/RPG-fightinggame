# Projekt: RPG-fightinggame | Modul: interactions
# Author: Ali Abas Arsalahn
# Datum: 26.04.2022

"""This module hosts interactions between character objects"""

from random import randrange


class Interactions:
    """
    Interactions class. Contains generic Methods, that characters can use.
    Methods: roll_dice, combat, speak
    """
    def roll_dice(max_range: int) -> int:
        """Returns a random integer"""
        return randrange(1, max_range)

    # incomplete
    def combat(object_1: object, object_2: object) -> None:
        """Combat function."""
        both_combatants_alive = True
        while both_combatants_alive:
            pass

        def speak(self) -> tuple:
        """checks intelligence attributes and allows speach acording to the stat."""
        intelligence = self.attributes.get("intelligence")
        if intelligence > 3:
            can_speak_to_peasants = True
        if intelligence > 5:
            can_speak_to_citizens = True
        if intelligence > 8:
            can_speak_to_nobles = True

        speech = (can_speak_to_peasants,
                  can_speak_to_citizens, can_speak_to_nobles)
        return speech