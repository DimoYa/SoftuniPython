from unittest import TestCase, main
from project.furniture import Furniture


class FurnitureTests(TestCase):

    def setUp(self):
        self.furniture = Furniture("TestFurniture", 10.00, (1, 2, 3))

    def test_init_default(self):
        self.assertEqual("TestFurniture", self.furniture.model)
        self.assertEqual(10.00, self.furniture.price)
        self.assertEqual((1, 2, 3), self.furniture.dimensions)
        self.assertTrue(self.furniture.in_stock)
        self.assertEqual(None, self.furniture.weight)

    def test_init_set(self):
        f = Furniture("TestFurniture", 10.00, (1, 2, 3), False, 25)
        self.assertEqual("TestFurniture", f.model)
        self.assertEqual(10.00, f.price)
        self.assertEqual((1, 2, 3), f.dimensions)
        self.assertFalse(f.in_stock)
        self.assertEqual(25, f.weight)

    def test_invalid_model_raise(self):
        with self.assertRaises(Exception) as ex:
            Furniture("  ", 10.00, (1, 2, 3))
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(Exception) as ex:
            Furniture("a" * 51, 10.00, (1, 2, 3))
        self.assertEqual(str(ex.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_invalid_price_raise(self):
        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", -1.0, (1, 2, 3))
        self.assertEqual(str(ex.exception), "Price must be a non-negative number.")

        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", -1.0, (1, 2, 3))
        self.assertEqual(str(ex.exception), "Price must be a non-negative number.")

    def test_invalid_dimensions_raise(self):
        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", 10.00, (1, 2, 3, 4))
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", 10.00, (-1, -1, -1))
        self.assertEqual(str(ex.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_invalid_weight_raise(self):
        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", 10.0, (1, 2, 3), True, 0.0)
        self.assertEqual(str(ex.exception), "Weight must be greater than zero.")

        with self.assertRaises(Exception) as ex:
            f = Furniture("TestFurniture", 10.0, (1, 2, 3), True, -1.0)
        self.assertEqual(str(ex.exception), "Weight must be greater than zero.")

    def test_status_not_in_stock(self):
        self.furniture.in_stock = False

        actual = self.furniture.get_available_status()

        self.assertEqual("Model: TestFurniture is currently unavailable.", actual)

    def test_status_in_stock(self):
        actual = self.furniture.get_available_status()

        self.assertEqual("Model: TestFurniture is currently in stock.", actual)

    def test_specifications_not_weight(self):
        actual = self.furniture.get_specifications()

        self.assertEqual("Model: TestFurniture has the following dimensions: 1mm x 2mm x 3mm and weighs: N/A", actual)

    def test_specifications_weight(self):
        self.furniture.weight = 20.0

        actual = self.furniture.get_specifications()

        self.assertEqual("Model: TestFurniture has the following dimensions: 1mm x 2mm x 3mm and weighs: 20.0", actual)


if __name__ == "__main__":
    main()
