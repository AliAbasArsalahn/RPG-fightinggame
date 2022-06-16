"""
rogue module.
implementation: class rogue
imports: Character from character module
"""


from character import Character


class Rogue(Character):
    """
    Rogue class. Extends Character
    Methods: dagger_attack, stealth
    """

    def __init__(self) -> None:
        super().__init__()
        self.spells = {
            1: self.dagger_attack,
            2: self.stealth
        }

    def dagger_attack(self) -> int:
        """dagger_attack method. Calculates damage done and returns it as integer."""
        DAMAGE_MULIPLIER = 4
        ROLL_MULTIPLIER = 2
        damage = self.roll_dice(DAMAGE_MULIPLIER) * ROLL_MULTIPLIER
        return damage

    def stealth(self) -> None:
        pass
