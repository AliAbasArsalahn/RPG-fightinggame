"""attributes module."""


class Attributes():
    """
    Attributes class.
    Includes: level, experience, strength, intellect, agility, stamina
    methods:
    """

    def __init__(self) -> None:
        """sets attributes as None."""
        self._level: int = None
        self._experience: int = None
        self._strength: int = None
        self._intellect: int = None
        self._agility: int = None
        self._stamina: int = None
        self._mana: int = None

    @property
    def level(self) -> int:
        """returns level"""
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        """sets level if value is not lesser than or equals to 0."""
        if value >= 0:
            self._level = value

    @property
    def experience(self) -> int:
        """returns experience."""
        return self._experience

    @experience.setter
    def experience(self, value: int) -> None:
        """sets experience if value is not 0 or lesser than 0."""
        if value > 0:
            self._experience = value

    @property
    def strength(self) -> int:
        """returns strength."""
        return self._strength

    @strength.setter
    def strength(self, value: int) -> None:
        """sets strength if value is not 0 or less than 0."""
        if value >= 0:
            self._strength = value

    @property
    def intellect(self) -> int:
        """returns intellect"""
        return self._intellect

    @intellect.setter
    def intellect(self, value: int) -> None:
        """sets intellect if value is not 0 or less than 0."""
        if value > 0:
            self._intellect = value

    @property
    def agility(self) -> int:
        """returns agility."""
        return self._agility

    @agility.setter
    def agility(self, value: int) -> None:
        """sets agility if value is not 0 or less than 0."""
        if value >= 0:
            self._agility = value

    @property
    def stamina(self) -> int:
        """returns stamina."""
        return self._stamina

    @stamina.setter
    def stamina(self, value: int) -> None:
        """sets stamina if stamina is not 0 or less than 0."""
        if value > 0:
            self._stamina = value

    @property
    def mana(self) -> int:
        """returns mana."""
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        """Sets mana if value is """
        MAX_MANA = self.intellect * 10
        self._mana = value
        if self._mana > MAX_MANA:
            self._mana = MAX_MANA
        if self._mana < 0:
            self._mana = 0

    def levelup(self) -> None:
        """
        Checks if experience has reached a treshold.
        Increases character level if so.
        """
        pass
