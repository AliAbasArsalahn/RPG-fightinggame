"""combat module"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from character import Character


class Combat:
    """Combat-Interactions class"""
    @staticmethod
    def spellbook(spells: dict) -> None:
        """
        lists available spells and allows to choose.
        Takes available spells as argument.

        """
    def list_spellbooks(*args: list[Character]) -> None:
        for character in args:
            print(character.spellbook)

        spell_index = 1
        for spell in spells:
            print(f" {spell_index} {spells[spell]}")
            spell_index += 1
        spell_select = int(input("choose one ablity! "))
        spells[spell_select]()
