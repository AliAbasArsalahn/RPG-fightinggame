"""Race module"""


class Race():
    """Race Class. Component of characters and non-character objects"""

    def __init__(self) -> None:
        """
        Race object gets created with an array of available races,
        the selected race and it's linked perk.
        """
        self.AVAILABLE_RACES: list[str] = ['Human', 'Dwarf', 'Elf']
        self._race: str = None
        self.perk: object = None

    @property
    def race(self) -> None:
        return self._race

    @race.setter
    def race(self, value: str) -> None:
        if value in self.AVAILABLE_RACES:
            self._race = value
