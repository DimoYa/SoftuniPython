from unittest import TestCase, main
from project.mammal import Mammal


class MammalTests(TestCase):
    name = "test"
    type = "test_type"
    sound = "test_sound"

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_init(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("test makes test_sound", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("test is of type test_type", self.mammal.info())


if __name__ == '__main__':
    main()
