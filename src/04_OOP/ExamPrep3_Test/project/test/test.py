from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TennisPlayerTest(TestCase):
    def setUp(self):
        self.tennis_pl = TennisPlayer("Iva", 20, 10)

    def test_init_default(self):
        self.assertEqual("Iva", self.tennis_pl.name)
        self.assertEqual(20, self.tennis_pl.age)
        self.assertEqual(10, self.tennis_pl.points)
        self.assertEqual([], self.tennis_pl.wins)

    def test_invalid_name_raise(self):
        with self.assertRaises(Exception) as ex:
            TennisPlayer("Te", 20, 10)
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_invalid_age_raise(self):
        with self.assertRaises(Exception) as ex:
            TennisPlayer("Tes", 17, 10)
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_win_existing_raise(self):
        self.tennis_pl.wins.append("TestWin")

        actual = self.tennis_pl.add_new_win("TestWin")

        self.assertEqual("TestWin has been already added to the list of wins!", actual)

    def test_add_win_success(self):
        actual = self.tennis_pl.add_new_win("TestWin")

        self.assertEqual("TestWin", self.tennis_pl.wins[0])

    def test_lt_self_better(self):
        other = TennisPlayer("Other", 20, 9)

        actual = self.tennis_pl < other

        self.assertEqual("Iva is a better player than Other", actual)

    def test_lt_other_better(self):
        other = TennisPlayer("Other", 20, 11)

        actual = self.tennis_pl < other

        self.assertEqual("Other is a top seeded player and he/she is better than Iva", actual)

    def test_str(self):
        self.tennis_pl.wins.append("TestWin1")
        self.tennis_pl.wins.append("TestWin2")

        actual = self.tennis_pl.__str__()

        expected = f"Tennis Player: {self.tennis_pl.name}\n" \
                   f"Age: {self.tennis_pl.age}\n" \
                   f"Points: {self.tennis_pl.points:.1f}\n" \
                   f"Tournaments won: {', '.join(self.tennis_pl.wins)}"

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
