"""attributes module."""


class Attributes():
    """
    Attributes class.
    Includes: level, experience, strength, intellect, agility, stamina
    methods:
    """
    def __init__(self) -> None:
        """Constructor"""
        self._level: int = None
        self._experience: int = None
        self._strength: int = None
        self._intellect: int = None
        self._agility: int = None
        self._stamina: int = None
        self._mana: int = None
        # self._max_mana: int = None

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

    # @property
    # def max_mana(self) -> int:
    #     """max_mana getter"""
    #     return self._max_mana

    # @max_mana.setter
    # def max_mana(self) -> None:
    #     """
    #     max_mana setter. Each mage player gets 10 mana for every point in
    #     intelligence
    #     """
    #     MANA_MULTIPLIER = self.intellect * 10
    #     if self.intellect is not None:
    #         self._max_mana += MANA_MULTIPLIER

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        """Mana setter."""
        MAX_MANA = self.intellect * 10
        self._mana = value
        if self._mana > MAX_MANA:
            self._mana = MAX_MANA
        if self._mana < 0:
            self._mana = 0

    def levelup(self) -> None:
        pass