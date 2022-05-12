"""
Test_mage Module
"""


import unittest
from mage import Mage


class TestMage(unittest.TestCase):
    """
    Tests:
    """

    def setUp(self) -> None:
        self.test_mage = Mage('Gandalf', 'Human')

    def tearDown(self) -> None:
        pass

    def test_mana(self) -> None:
        self.assertTrue(self.test_mage._mana(20), self.test_mage._mana() == 20)


if __name__ == '__main__':
    unittest.main()
