"""
Test_mage Module
"""


import unittest
from mage import Mage
from rogue import Rogue


class TestMage(unittest.TestCase):
    """
    SetUp: Mage object and rogue object as test enemy
    Tests: mana, fireball, magic_missile
    """

    def setUp(self) -> None:
        self.mage = Mage()
        self.mage.attributes.strength = 10
        self.mage.attributes.intellect = 10
        self.mage.attributes.agility = 10
        self.mage.attributes.mana = 100

    def tearDown(self) -> None:
        pass

    def test_fireball(self) -> None:
        """
        Fireball damage is in expected range
        """
        self.assertTrue(self.mage.fireball() >=
                        2 and self.mage.fireball() <= 14)

    def test_magic_missile(self) -> None:
        """
        magic missile damage is in expected range
        """
        self.assertTrue(self.mage.magic_missile() >=
                        1 and self.mage.magic_missile() <= 6)


if __name__ == '__main__':
    unittest.main()
