from unittest import TestCase, main
# from main import Cat


class CatTests(TestCase):
    pass

    def setUp(self):
        self.c = Cat("Cat")

    def test_init(self):
        self.assertEqual(self.c.name, "Cat")
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(self.c.size, 0)

    def test_successfully_eat(self):
        # Act
        self.c.eat()

        # Assert
        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(self.c.size, 1)

    def test_already_fed(self):
        # Arrange
        self.c.eat()

        # Act & Assert
        with self.assertRaises(Exception) as ex:
            self.c.eat()

        # Assert Exception Message
        self.assertEqual(str(ex.exception), "Already fed.")

    def test_successfully_sleep(self):
        # Arrange
        self.c.eat()

        # Act
        self.c.sleep()

        # Assert
        self.assertFalse(self.c.sleepy)

    def test_cannot_sleep_hungry(self):
        # Act & Assert
        with self.assertRaises(Exception) as ex:
            self.c.sleep()

        # Assert Exception Message
        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")





if __name__ == '__main__':
    main()
