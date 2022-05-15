"""attributes module."""


class Attributes():
    """
    Attributes class.
    Includes: level, experience, strength, intellect, agility, stamina
    methods:
    """

    def __init__(self) -> None:
        """sets attributes as None."""
        self._stamina: int = None
        self._health: int = None
        self._max_health: int = None
        self._strength: int = None
        self._intellect: int = None
        self._level: int = None
        self._experience: int = None
        self._agility: int = None
        self._mana: int = None
        self._max_mana: int = None
        self._dodge_chance: float = None

    @property
    def health(self) -> int:
        """returns health."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """increases or decreases health."""
        self._health += value
        if self._health > self._max_health:
            self._health = self._max_health

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
        MANA_MULTIPLIER = 10
        self._max_mana = self._intellect * MANA_MULTIPLIER

    @property
    def mana(self) -> int:
        """returns mana."""
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        """Sets mana if value is """
        self._mana = value
        if self._mana > self._max_mana:
            self._mana = self._max_mana
        if self._mana < 0:
            self._mana = 0

    @property
    def agility(self) -> int:
        """returns agility."""
        return self._agility

    @agility.setter
    def agility(self, value: int) -> None:
        """sets agility if value is not 0 or less than 0."""
        if value >= 0:
            self._agility = value
        DODGE_CHANCE_MULTIPLIER = 0.01
        self._dodge_chance = self._agility * DODGE_CHANCE_MULTIPLIER

    @property
    def stamina(self) -> int:
        """returns stamina."""
        return self._stamina

    @stamina.setter
    def stamina(self, value: int) -> None:
        """sets stamina if stamina is not 0 or less than 0."""
        if value > 0:
            self._stamina = value
        HEALTH_MULTIPLIER = 10
        self._max_health = self._stamina * HEALTH_MULTIPLIER

    @property
    def dodge_chance(self) -> float:
        return self._dodge_chance

    @dodge_chance.setter
    def dodge_chance(self, value: float) -> None:
        """
        sets dodge chance as 1% for each point of agility.
        manipulates dodge_chance if a value is given.
        """
        if value:
            self._dodge_chance += value

    def levelup(self) -> None:
        """
        Checks if experience has reached a treshold.
        Increases character level if so.
        """
        pass
