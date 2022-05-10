# Projekt RPG-Fightinggame | Modul: test_mage
# Author: Ali Abas Arsalahn

"""
Test_mage Module
"""


import unittest
from .. import Mage


class TestMage(unittest.TestCase):
    """
    Tests:
    """

    def setUp(self) -> None:
        self.test_mage = Mage('Gandalf', 'Human')

    def tearDown(self) -> None:
        pass

    def test_mana(self) -> None:
        self.assertTrue(self.test_mage.mana(20), self.test_mage.mana() == 20)


if __name__ == '__main__':
    unittest.main()
