from unittest import TestCase, main
from main import IntegerList

class IntegerListTests(TestCase):
    def setUp(self):
        # Initialize a valid IntegerList instance for reuse
        self.valid_list = IntegerList(1, 2, 3, 4)

    def test_constructor_with_only_integers(self):
        obj = IntegerList(1, 2, 3, 4)
        self.assertEqual(obj._IntegerList__data, [1, 2, 3, 4])

    def test_constructor_with_mixed_types(self):
        obj = IntegerList(1, "two", 3.0, 4)
        self.assertEqual(obj._IntegerList__data, [1, 4])

    def test_constructor_with_no_args(self):
        obj = IntegerList()
        self.assertEqual(obj._IntegerList__data, [])

    def test_get_data(self):
        self.assertEqual(self.valid_list.get_data(), [1, 2, 3, 4])

    def test_add_non_int_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.valid_list.add("test")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_add_valid_int(self):
        result = self.valid_list.add(5)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(self.valid_list.get_data(), [1, 2, 3, 4, 5])

    def test_remove_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.valid_list.remove_index(10)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove_index_valid(self):
        removed = self.valid_list.remove_index(1)
        self.assertEqual(removed, 2)
        self.assertEqual(self.valid_list.get_data(), [1, 3, 4])

    def test_get_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.valid_list.get(10)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_valid_index(self):
        value = self.valid_list.get(2)
        self.assertEqual(value, 3)

    def test_insert_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.valid_list.insert(10, 5)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_non_int_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.valid_list.insert(1, "test")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_insert_valid(self):
        self.valid_list.insert(1, 5)
        self.assertEqual(self.valid_list.get_data(), [1, 5, 2, 3, 4])

    def test_get_biggest(self):
        self.assertEqual(self.valid_list.get_biggest(), 4)

    def test_get_biggest_empty_list_raises(self):
        empty_list = IntegerList()
        with self.assertRaises(IndexError):
            empty_list.get_biggest()

    def test_get_index(self):
        self.assertEqual(self.valid_list.get_index(2), 1)

    def test_get_index_not_in_list_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.valid_list.get_index(10)
        self.assertEqual(str(ex.exception), "10 is not in list")

    def test_remove_last_index(self):
        removed = self.valid_list.remove_index(len(self.valid_list.get_data()) - 1)
        self.assertEqual(removed, 4)
        self.assertEqual(self.valid_list.get_data(), [1, 2, 3])

    def test_empty_list_get_index_raises(self):
        empty_list = IntegerList()
        with self.assertRaises(ValueError):
            empty_list.get_index(1)


if __name__ == "__main__":
    main()
