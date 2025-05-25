from unittest import TestCase, main

from project.movie import Movie

class MovieTest(TestCase):
    def setUp(self):
        self.movie = Movie("TestName", 2000, 10)

    def test_init_default(self):
        self.assertEqual("TestName", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_invalid_name_raise(self):
        with self.assertRaises(Exception) as ex:
            Movie("", 2000, 10)
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_invalid_year_raise(self):
        with self.assertRaises(Exception) as ex:
            Movie("Test", 1886, 10)
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_add_actor_existing_actor(self):
        self.movie.add_actor("Brad Pitt")
        actual = self.movie.add_actor("Brad Pitt")

        self.assertEqual(actual, "Brad Pitt is already added in the list of actors!")
        self.assertEqual(self.movie.actors, ["Brad Pitt"])

    def test_add_actor_valid(self):
        self.movie.add_actor("Brad Pitt")
        actual = self.movie.add_actor("Angelina Jolie")

        self.assertEqual(self.movie.actors, ["Brad Pitt", "Angelina Jolie"])

    def test_gt_self_is_gt(self):
        other = Movie("TestName2", 2000, 9.9)

        actual = self.movie.__gt__(other)

        self.assertEqual(actual, '"TestName" is better than "TestName2"')

    def test_gt_other_is_gt(self):
        other = Movie("TestName2", 2000, 10.1)

        actual = self.movie.__gt__(other)

        self.assertEqual(actual, '"TestName2" is better than "TestName"')

    def test_repr(self):
        self.movie.add_actor("Brad Pitt")
        self.movie.add_actor("Angelina Jolie")
        actual = self.movie.__repr__()

        self.assertEqual(actual, "Name: TestName\nYear of Release: 2000\nRating: 10.00\nCast: Brad Pitt, Angelina Jolie")

if __name__ == "__main__":
        main()