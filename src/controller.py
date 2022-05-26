"""controller module."""


class Controller:
    """Controller class"""
    @staticmethod
    def health_increase(character: object, amount: int) -> None:
        character.health += amount
