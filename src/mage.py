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

    def __init__(self) -> None:
        """Mage constructor."""

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
        self.attributes.dodge_chance += 0.5

    def healing(self) -> None:
        """calls function roll dice. Increases current_health by that amount"""
        self.attributes.current_health += self.interactions.roll_dice(5)
