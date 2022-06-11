"""combat module"""

from typing import TYPE_CHECKING
class Combat:
    """Combat-Interactions class"""
    @staticmethod
    def spellbook(spells: dict) -> None:
        """
        lists available spells and allows to choose.
        Takes available spells as argument.
        
        """
        spell_index = 1
        for spell in spells:
            print(f" {spell_index} {spells[spell]}")