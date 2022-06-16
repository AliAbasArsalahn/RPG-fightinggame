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
        spell_index = 1
        for spell in spells:
            print(f" {spell_index} {spells[spell]}")
            spell_index += 1
        spell_select = int(input("choose one ablity! "))
        spells[spell_select]()

    @staticmethod
    def list_spellbook(*args: list[Character]) -> None:
        for character in args:
            character.spellbook()
            # print(character.spellbook)
