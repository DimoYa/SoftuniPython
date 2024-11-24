from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    pass

    def setUp(self):
        self.car = Vehicle(100, 150)

    def test_init(self):
        self.assertEqual(100, self.car.fuel)
        self.assertEqual(150, self.car.horse_power)
        self.assertEqual(100, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_not_enough_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(81)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_enough_fuel(self):
        # Act
        self.car.drive(80)

        # Assert
        self.assertEqual(0, self.car.fuel)

    def test_refuel_too_much_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(1)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_enough_capacity(self):
        # Act
        self.car.refuel(0)

        # Assert
        self.assertEqual(100, self.car.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 150 horse power"
                         " with 100 fuel left and 1.25 fuel consumption", self.car.__str__())


if __name__ == '__main__':
    main()
