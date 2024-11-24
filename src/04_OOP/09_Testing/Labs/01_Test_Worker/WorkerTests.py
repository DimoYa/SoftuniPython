from unittest import TestCase, main
from main import Worker


class WorkerTests(TestCase):
    pass

    def setUp(self):
        self.w = Worker("Test", 1000, 100)

    def test_init(self):
        self.assertEqual(self.w.name, "Test")
        self.assertEqual(self.w.salary, 1000)
        self.assertEqual(self.w.energy, 100)
        self.assertEqual(self.w.money, 0)

    def test_not_enough_energy(self):
        # Arrange
        self.w.energy = -1

        # Act & Assert
        with self.assertRaises(Exception) as ex:
            self.w.work()

        # Assert Exception Message
        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_enough_energy(self):
        # Act
        self.w.work()

        # Assert
        self.assertEqual(self.w.money, 1000)
        self.assertEqual(self.w.energy, 99)

    def test_rest(self):
        # Act
        self.w.rest()

        # Assert
        self.assertEqual(self.w.energy, 101)

    def test_get_info(self):
        # Act
        self.w.work()
        actual = self.w.get_info()

        # Assert
        self.assertEqual(actual, 'Test has saved 1000 money.')


if __name__ == '__main__':
    main()
