"""controller module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


class Controller:
    """Controller class"""
    @staticmethod
    def health_increase(character: Character, amount: int) -> None:
        character.attributes.health += amount
