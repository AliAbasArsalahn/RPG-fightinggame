"""Race module"""


class Race():
    """Race Class. Component of characters and non-character objects"""

    def __init__(self) -> None:
        self.AVAILABLE_RACES = ['Human', 'Dwarf', 'Elf']
        self._race = None
        self.perk = None

    @property
    def race(self) -> None:
        return self._race

    @race.setter
    def race(self, value: str) -> None:
        if value in self.AVAILABLE_RACES:
            self._race = value
