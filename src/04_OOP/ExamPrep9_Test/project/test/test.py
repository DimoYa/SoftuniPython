from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class RailwayStationTest(TestCase):
    def setUp(self):
        self.railway = RailwayStation("Test")

    def test_init_default(self):
        self.assertEqual("Test", self.railway.name)
        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_invalid_name_raise(self):
        with self.assertRaises(Exception) as ex:
            RailwayStation("TES")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_arrival_on_board(self):
        first_train_info = "First Test Train Info"
        self.railway.new_arrival_on_board(first_train_info)

        second_train_info = "Second Test Train Info"
        self.railway.new_arrival_on_board(second_train_info)

        self.assertEqual(self.railway.arrival_trains[0], first_train_info)
        self.assertEqual(len(self.railway.arrival_trains), 2)

    def test_train_has_arrived_one(self):
        first_train_info = "First Test Train Info"
        self.railway.new_arrival_on_board(first_train_info)

        result = self.railway.train_has_arrived(first_train_info)

        self.assertEqual(result, f"{first_train_info} is on the platform and will leave in 5 minutes.")
        self.assertEqual(len(self.railway.departure_trains), 1)

    def test_train_has_arrived_more(self):
        first_train_info = "First Test Train Info"
        self.railway.new_arrival_on_board(first_train_info)

        result = self.railway.train_has_arrived("Another Test Train Info")

        self.assertEqual(result, f"There are other trains to arrive before Another Test Train Info.")
        self.assertEqual(len(self.railway.departure_trains), 0)

    def test_train_has_left_true(self):
        train_info = "First Test Train Info"
        self.railway.new_arrival_on_board(train_info)
        self.railway.train_has_arrived(train_info)

        result = self.railway.train_has_left(train_info)

        self.assertEqual(result, True)
        self.assertEqual(len(self.railway.departure_trains), 0)

    def test_train_has_left_false(self):
        first_train_info = "First Test Train Info"
        self.railway.new_arrival_on_board(first_train_info)
        self.railway.train_has_arrived(first_train_info)

        second_train_info = "Second Test Train Info"
        self.railway.new_arrival_on_board(second_train_info)
        self.railway.train_has_arrived(second_train_info)

        result = self.railway.train_has_left(second_train_info)

        self.assertEqual(result, False)
        self.assertEqual(len(self.railway.departure_trains), 2)


