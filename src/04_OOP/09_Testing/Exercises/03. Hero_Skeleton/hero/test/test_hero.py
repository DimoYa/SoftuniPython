from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero("test", 100, 50, 10)
        self.enemy = Hero("enemy", 120, 70, 20)

    def test_init(self):
        self.assertEqual("test", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_cannot_fight_battle_raise(self):
        # Arrange
        self.enemy.username = "test"

        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_lower_than_zero_health_raise(self):
        # Arrange
        self.hero.health = 0

        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

        # Arrange
        self.hero.health = -1

        # Act and Assert
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_lower_than_zero_health_enemy_raise(self):
        # Arrange
        self.enemy.health = 0

        # Act and Assert
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight enemy. He needs to rest")

        # Arrange
        self.enemy.health = -1

        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight enemy. He needs to rest")

    def test_battle_draw(self):
        # Act
        result = self.hero.battle(self.enemy)

        # Assert
        self.assertEqual(-2350, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(-930, self.enemy.health)
        self.assertEqual(20, self.enemy.damage)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        # Arrange
        self.hero.health = 3000
        # Act
        result = self.hero.battle(self.enemy)

        # Assert
        self.assertEqual(605, self.hero.health)
        self.assertEqual(15, self.hero.damage)
        self.assertEqual(-930, self.enemy.health)
        self.assertEqual(20, self.enemy.damage)
        self.assertEqual("You win", result)

    def test_battle_lose(self):
        # Arrange
        self.enemy.health = 3000
        # Act
        result = self.hero.battle(self.enemy)

        # Assert
        self.assertEqual(-2350, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual(2005, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        self.assertEqual("Hero test: 100 lvl\nHealth: 50\nDamage: 10\n", self.hero.__str__())


if __name__ == "__main__":
    main()
