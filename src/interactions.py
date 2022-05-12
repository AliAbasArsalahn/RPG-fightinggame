# Projekt: RPG-fightinggame | Modul: interactions
# Author: Ali Abas Arsalahn
# Datum: 26.04.2022

"""This module hosts interactions between character objects"""

from random import randrange

def roll_dice(max_range: int) -> int:
    """Returns a random integer"""
    return randrange(1, max_range)


def combat(object_1: object, object_2: object) -> None:
    """Combat function."""
    both_combatants_alive = True
    while both_combatants_alive:
        pass
