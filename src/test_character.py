"""Character Test Module"""


from character import Character
import unittest


class TestCharacter(unittest.TestCase):
    """
    Tests:
    """

    def setUp(self) -> None:
        self.character = Character()
        self.character.attributes.stamina = 10
        self.character.attributes.strength = 10
        self.character.attributes.intellect = 10
        self.character.attributes.agility = 10
        self.character.attributes.experience = 1000

    def tearDown(self) -> None:
        pass

    def test_max_health(self) -> None:
        self.assertTrue(self.character.attributes._max_health == 100)

    def test_dodge_chance(self) -> None:
        self.assertTrue(self.character.attributes._dodge_chance == 0.1)

    def test_mana(self) -> None:
        pass

    def test_level(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
