"""controller module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character
    from display import Display


class Controller:
    """Controller class"""
    @staticmethod
    def health_increase(character: Character, amount: int) -> None:
        character.attributes.health += amount
