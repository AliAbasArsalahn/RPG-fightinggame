"""
Module: Mage.
implementes methods and attributes for the mage class.
"""
from character import Character


class Mage(Character):
    """
    class: mage
    methods: Fireball, magic missile
    properties: max_mana, mana
    """

    def __init__(self, name: str, race: str) -> None:
        """Mage constructor."""
        super().__init__(name, race)
        self._mana: int = None
        self._max_mana: int = None

    @property
    def max_mana(self) -> int:
        """max_mana getter"""
        return self._max_mana

    @max_mana.setter
    def max_mana(self) -> None:
        """
        max_mana setter. Each mage player gets 10 mana for every point in
        intelligence
        """
        if self._attributes["intellect"] > 0:
            self._max_mana = self._attributes["intellect"] * 10

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int) -> None:
        """Mana setter."""
        self._mana += value
        if self._mana > self._max_mana:
            self._mana = self._max_mana
        if self._mana < 0:
            self._mana = 0

    def fireball(self, other: object) -> None:
        """fireball. Damage=2d7"""
        fireball_dmg = self.interactions.roll_dice(8) * 2
        other.current_health -= fireball_dmg

    def magic_missile(self, other: object) -> None:
        """magic missile. Damage=1d6"""
        magic_missile_damage = self.roll_dice(7)
        other.current_health -= magic_missile_damage

    def mirror_images(self) -> None:
        """increases self.dodgechance for 2 rounds by 50%"""
        self.dodge_chance += 0.5

    def healing(self) -> None:
        """calls function roll dice. Increases current_health by that amount"""
        self.current_health += self.roll_dice(5)
