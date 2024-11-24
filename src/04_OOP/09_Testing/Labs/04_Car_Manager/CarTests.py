from unittest import TestCase, main
# from main import Car


class CarTests(TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Corolla", 6.0, 50)

    def test_init_valid(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Corolla")
        self.assertEqual(self.car.fuel_consumption, 6.0)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_init_null_empty_make_raise(self):
        with self.assertRaises(Exception) as ex:
            Car("", "Corolla", 6.0, 50)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_init_null_empty_model_raise(self):
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "", 6.0, 50)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_negative_zero_fuel_cons_raise(self):
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Corolla", 0, 50)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Corolla", -1, 50)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_negative_zero_fuel_capacity_raise(self):
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Corolla", 50, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Corolla", 50, -1)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_negative_refuel_with_zero_negative_raise(self):
        # Arrange
        car = Car("Toyota", "Corolla", 50, 10)

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")


    def test_refuel_with_more_than_capacity(self):
        # Arrange
        car = Car("Toyota", "Corolla", 50, 10)

        # Act
        car.refuel(11)

        # Assert
        self.assertEqual(car.fuel_amount, 10)

    def test_refuel_with_less_than_capacity(self):
        # Arrange
        car = Car("Toyota", "Corolla", 50, 10)

        # Act
        car.refuel(8)

        # Assert
        self.assertEqual(car.fuel_amount, 8)


    def test_drive_not_enough_fuel_raise(self):
        # Arrange
        car = Car("Toyota", "Corolla", 50, 10)
        car.fuel_amount = 4

        with self.assertRaises(Exception) as ex:
            car.drive(10)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel_raise(self):
        # Arrange
        car = Car("Toyota", "Corolla", 50, 10)
        car.fuel_amount = 5

        # Act
        car.drive(10)

        # Assert
        self.assertEqual(car.fuel_amount, 0)


if __name__ == "__main__":
    main()
