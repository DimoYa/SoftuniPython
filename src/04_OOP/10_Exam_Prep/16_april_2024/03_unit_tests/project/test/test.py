from unittest import TestCase, main

from project.restaurant import Restaurant


class RestaurantTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("Valid", 1)
        self.waiters_test = [
            {'name': 'Alice', 'total_earnings': 100},
            {'name': 'Bob', 'total_earnings': 200},
            {'name': 'Charlie', 'total_earnings': 150},
            {'name': 'David', 'total_earnings': 50},
            {'name': 'Eve'},  # Missing total_earnings key
            {'name': 'Frank', 'total_earnings': 0}
        ]

    def test_init(self):
        self.assertEqual("Valid", self.restaurant.name)
        self.assertEqual(1, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_invalid_name_raise(self):
        with self.assertRaises(Exception) as ex:
            Restaurant("", 1)
        self.assertEqual(str(ex.exception), "Invalid name!")

    def test_invalid_capacity_raise(self):
        with self.assertRaises(Exception) as ex:
            Restaurant("Valid", -1)
        self.assertEqual(str(ex.exception), "Invalid capacity!")

    def test_get_waiters_empty(self):
        actual = self.restaurant.get_waiters(1, 10)

        self.assertEqual([], actual)

    def test_get_waiters_success(self):
        actual = self.restaurant.get_waiters(1, 10)

        self.assertEqual([], actual)

    def test_min_earnings_filter_only(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.get_waiters(min_earnings=100)
        expected = [
            {'name': 'Alice', 'total_earnings': 100},
            {'name': 'Bob', 'total_earnings': 200},
            {'name': 'Charlie', 'total_earnings': 150}
        ]
        self.assertEqual(result, expected)

    def test_max_earnings_filter_only(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.get_waiters(max_earnings=100)
        expected = [
            {'name': 'Alice', 'total_earnings': 100},
            {'name': 'David', 'total_earnings': 50},
            {'name': 'Eve'},
            {'name': 'Frank', 'total_earnings': 0}
        ]
        self.assertEqual(result, expected)

    def test_both_min_and_max_earnings_filter(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.get_waiters(min_earnings=75, max_earnings=175)
        expected = [
            {'name': 'Alice', 'total_earnings': 100},
            {'name': 'Charlie', 'total_earnings': 150}
        ]
        self.assertEqual(result, expected)

    def test_remove_filter_not_found(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.remove_waiter("invalid")

        self.assertEqual(result, "No waiter found with the name invalid.")
        self.assertEqual(self.waiters_test, self.restaurant.waiters)

    def test_remove_filter_success(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.remove_waiter("Alice")

        self.assertEqual(result, "The waiter Alice has been removed.")
        self.assertEqual(self.waiters_test, self.restaurant.waiters)


    def test_get_total_earnings_success(self):
        self.restaurant.waiters = self.waiters_test
        result = self.restaurant.get_total_earnings()

        self.assertEqual(result, 500)

    def test_get_total_earnings_zero(self):
        result = self.restaurant.get_total_earnings()

        self.assertEqual(result, 0)

if __name__ == "__main__":
    main()

