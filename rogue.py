# Projekt: RPG-fightinggame | Modul: Rogue
# Author: Ali Abas Arsalahn
# Datum: 25.04.2022
"""
rogue module.
implementation: class rogue
imports: Character from character module
"""


from character import Character


class Rogue(Character):
    """
    Rogue class.
    Methods: dagger_attack
    Properties:
    """

    def dagger_attack(self) -> int:
        """dagger_attack method. Calculates damage done and returns it as integer."""
        damage = self.roll_dice(5) * 2
        return damage

    def stealth(self) -> None:
        pass
