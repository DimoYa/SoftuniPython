from unittest import TestCase, main

from project.shopping_cart import ShoppingCart

class ShoppingCartTest(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("TestName", 150)

    def test_init_default(self):
        self.assertEqual("TestName", self.shopping_cart.shop_name)
        self.assertEqual(150, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_invalid_name_raise(self):
        with self.assertRaises(Exception) as ex:
            ShoppingCart("test", 150)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(Exception) as ex:
            ShoppingCart("Test1", 150)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_name_setter_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "invalidName"
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = "Name1"
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_too_expensive_raise(self):
        with self.assertRaises(Exception) as ex:
            self.shopping_cart.add_to_cart("test", 100)
        self.assertEqual(str(ex.exception), "Product test cost too much!")
        self.assertEqual(len(self.shopping_cart.products), 0)

    def test_add_to_cart_success(self):
        actual = self.shopping_cart.add_to_cart("test", 99)

        self.assertEqual(actual, "test product was successfully added to the cart!")
        self.assertEqual(self.shopping_cart.products, {"test": 99})
        self.assertEqual(len(self.shopping_cart.products), 1)

    def test_add_cart_product_conflict_overwrites(self):
        self.shopping_cart.add_to_cart("SharedProduct", 10)
        other_cart = ShoppingCart("Another", 100)
        other_cart.add_to_cart("SharedProduct", 50)

        combined = self.shopping_cart + other_cart

        self.assertEqual(combined.products["SharedProduct"], 50)

    def test_remove_nonexistent_raise(self):
        self.shopping_cart.add_to_cart("test", 99)
        with self.assertRaises(Exception) as ex:
            self.shopping_cart.remove_from_cart("another")
        self.assertEqual(str(ex.exception), "No product with name another in the cart!")
        self.assertEqual(len(self.shopping_cart.products), 1)
        self.assertEqual(self.shopping_cart.products, {"test": 99})

    def test_remove_from_cart_success(self):
        self.shopping_cart.add_to_cart("test1", 99)
        self.shopping_cart.add_to_cart("test2", 99)

        actual = self.shopping_cart.remove_from_cart("test1")

        self.assertEqual(actual, "Product test1 was successfully removed from the cart!")
        self.assertEqual(len(self.shopping_cart.products), 1)
        self.assertEqual(self.shopping_cart.products, {"test2": 99})

    def test_add_success(self):
        self.shopping_cart.add_to_cart("Product1", 20)
        other_shop_cart = ShoppingCart("AnotherTest", 200)
        other_shop_cart.products = {"Product2": 50, "Product3": 30}

        actual = self.shopping_cart.__add__(other_shop_cart)
        self.assertEqual(actual.shop_name, "TestNameAnotherTest")
        self.assertEqual(actual.budget, 350)
        self.assertEqual(actual.products, {'Product1': 20, 'Product2': 50, 'Product3': 30})

    def test_buy_products_not_enough_money_raise(self):
        self.shopping_cart.add_to_cart("Product1", 90)
        self.shopping_cart.add_to_cart("Product2", 90)
        with self.assertRaises(Exception) as ex:
            self.shopping_cart.buy_products()
        self.assertEqual(str(ex.exception), "Not enough money to buy the products! Over budget with 30.00lv!")
        self.assertEqual(len(self.shopping_cart.products), 2)
        self.assertEqual(self.shopping_cart.products, {'Product1': 90, 'Product2': 90})

    def test_buy_products_success(self):
        self.shopping_cart.add_to_cart("Product1", 20)
        self.shopping_cart.add_to_cart("Product2", 35)

        actual = self.shopping_cart.buy_products()

        self.assertEqual(actual, "Products were successfully bought! Total cost: 55.00lv.")
        self.assertEqual(len(self.shopping_cart.products), 2)
        self.assertEqual(self.shopping_cart.products, {'Product1': 20, 'Product2': 35})


if __name__ == "__main__":
        main()