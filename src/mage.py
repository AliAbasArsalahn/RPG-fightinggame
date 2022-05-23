"""
Module: Mage.
implementes methods and attributes for the mage class.
"""
from character import Character


class Mage(Character):
    """
    class: mage
    methods: Fireball, magic missile, mirror images, healing
    inherits: Name, race, attributes, interactions from character.
    """

    def fireball(self, target: object) -> None:
        """computes fireball damage. Damage=2d7"""
        ROLL_MULTIPLIER = 2
        DAMAGE_MULTIPLIER = 7
        fireball_dmg = self.interactions.roll_dice(
            DAMAGE_MULTIPLIER) * ROLL_MULTIPLIER
        target.health -= fireball_dmg

    def magic_missile(self, target: object) -> None:
        """computes magic missile damage. Damage=1d6"""
        DAMAGE_MULTIPLIER = 6
        magic_missile_damage = self.roll_dice(DAMAGE_MULTIPLIER)
        target.health -= magic_missile_damage

    def mirror_images(self) -> None:
        """increases self.dodgechance for 2 rounds by 50%"""
        DODGE_INCREASE = 0.5
        self.attributes.dodge_chance += DODGE_INCREASE

    def healing(self) -> None:
        """calls function roll dice. Increases current_health by that amount"""
        HEALING_MULTIPLIER = 4
        self.attributes.current_health += self.interactions.roll_dice(
            HEALING_MULTIPLIER)
