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

    def tearDown(self) -> None:
        pass

    def test_max_health(self) -> None:
        self.assertTrue(self.character.attributes.stamina == 10)


if __name__ == '__main__':
    unittest.main()
