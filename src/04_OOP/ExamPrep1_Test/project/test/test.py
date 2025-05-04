from unittest import TestCase, main

from project.soccer_player import SoccerPlayer


class SoccerPlayerTests(TestCase):
    _VALID_TEAMS = ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"]

    def setUp(self):
        self.soccer = SoccerPlayer("Name11", 16, 0, "Barcelona")
        self.other = SoccerPlayer("Name12", 16, 1, "Barcelona")

    def test_init(self):
        self.assertEqual("Name11", self.soccer.name)
        self.assertEqual(16, self.soccer.age)
        self.assertEqual(0, self.soccer.goals)
        self.assertEqual("Barcelona", self.soccer.team)
        self.assertEqual({}, self.soccer.achievements)
        self.assertEqual(self._VALID_TEAMS, SoccerPlayerTests._VALID_TEAMS)

    def test_short_name_raise(self):
        with self.assertRaises(Exception) as ex:
            SoccerPlayer("Name1", 20, 10, "Barcelona")
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(Exception) as ex:
            SoccerPlayer("Name", 20, 10, "Barcelona")
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_invalid_age_raise(self):
        with self.assertRaises(Exception) as ex:
            SoccerPlayer("Name11", 15, 10, "Barcelona")
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_invalid_goals_raise(self):
        soccer = SoccerPlayer("Name11", 16, -1, "Barcelona")
        self.assertEqual(0, soccer.goals)

    def test_invalid_team_raise(self):
        with self.assertRaises(Exception) as ex:
            SoccerPlayer("Name11", 16, 0, "Test")
        self.assertEqual(str(ex.exception), f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!")

    def test_change_team_not_found_raise(self):
        actual = self.soccer.change_team("Invalid")
        self.assertEqual("Invalid team name!", actual)

    def test_change_team_success(self):
        new_team = "Real Madrid"

        result = self.soccer.change_team(new_team)

        self.assertEqual(new_team, self.soccer.team)
        self.assertEqual("Team successfully changed!", result)

    def test_add_achievement_non_existing(self):
        result = self.soccer.add_new_achievement("New")

        self.assertEqual({"New": 1}, self.soccer.achievements)
        self.assertEqual("New has been successfully added to the achievements collection!",
                         result)

    def test_add_achievement_existing(self):
        self.soccer.add_new_achievement("New")
        self.soccer.add_new_achievement("New")

        self.assertEqual({"New": 2}, self.soccer.achievements)

    def test_lt_other_more(self):
        result = self.soccer < self.other
        self.assertEqual("Name12 is a top goal scorer! S/he scored more than Name11.", result)

    def test_lt_other_less(self):
        self.soccer.goals = 3
        result = self.soccer < self.other
        self.assertEqual("Name11 is a better goal scorer than Name12.", result)


if __name__ == "__main__":
    main()

