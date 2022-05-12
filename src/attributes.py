"""attributes module."""


class Attributes():
    """
    Attributes class.
    Includes: level, experience, strength, intellect, agility, stamina
    """
    def __init__(self) -> None:
        """Constructor"""
        self._level: int = None
        self._experience: int = None
        self._strength: int = None
        self._intellect: int = None
        self._agility: int = None
        self._stamina: int = None

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        if value > 0:
            self._level = value

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, value: int) -> None:
        if value > 0:
            self._experience = value

    @property
    def strength(self) -> int:
        return self._strength

    @strength.setter
    def strength(self, value: int) -> None:
        if value > 0:
            self._strength = value

    @property
    def intellect(self) -> int:
        return self._intellect

    @intellect.setter
    def intellect(self, value: int) -> None:
        if value > 0:
            self._intellect = value

    @property
    def agility(self) -> int:
        return self._agility

    @agility.setter
    def agility(self, value: int) -> None:
        if value > 0:
            self._agility = value

    @property
    def stamina(self) -> int:
        return self._stamina

    @stamina.setter
    def stamina(self, value: int) -> None:
        if value > 0:
            self._stamina = value