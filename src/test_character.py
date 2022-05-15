"""Character Test Module"""


from character import Character
import unittest

class TestCharacter(unittest.TestCase):
    """
    Tests:
    """
    def setUp(self) -> None:
        self.character = Character()
        self.character.attributes.agility = 10

    def tearDown(self) -> None:
        pass

    def test_fireball(self) -> None:
        pass
