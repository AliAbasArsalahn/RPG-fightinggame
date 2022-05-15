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
        self.mage = Mage()
        self.mage.attributes.
        self.mage.attributes.intellect = 10
        self.mage.attributes.mana = 100

    def tearDown(self) -> None:
        pass

    def test_mana(self) -> None:
        self.assertTrue(self.mage.attributes.mana == 100)


if __name__ == '__main__':
    unittest.main()
