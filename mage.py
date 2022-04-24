# Projekt RPG-fightinggame \ Modul: mage
# Author: Ali Abas Arsalahn
# Datum: 21.04.2022

"""
Module: Mage.
implementes methods and attributes for the mage class.
"""


from character import Character

class Mage(Character):
    """
    class: mage
    methods: Fireball, 
    properties: max_mana, mana
    """

    def __init__(self, name: str, race: str) -> object:
        super().__init__(name, race)

    @property
    def max_mana(self) -> int:
        """max_mana getter"""
        return self.max_mana

    @max_mana.setter
    def max_mana(self) -> None:
        """
        max_mana setter. Each mage player gets 10 mana for every point in 
        intelligence
        """
        if self.attributes["intellect"] > 0:
            self.max_mana = self.attributes["intellect"] * 10

    @property
    def mana(self) -> int:
        return self.mana

    @mana.setter
    def mana(self, value: int) -> None:
        """"""
        self.mana += value
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        if self.mana < 0:
            self.mana = 0

    def fireball(self, other: object) -> None:
        """fireball. Damage=2d7"""
        fireball_dmg = self.roll_dice(1, 8) + 2
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
