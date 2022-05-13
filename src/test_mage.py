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
        self.test_mage.mana = 100

    def tearDown(self) -> None:
        pass

    def test_mana(self) -> None:
        self.assertTrue(self.test_mage.mana -= 10, self.test_mage.mana == 90)


if __name__ == '__main__':
    unittest.main()
