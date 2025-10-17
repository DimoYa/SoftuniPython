from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "TestType", 10, 10)

    def test_init_default(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("TestType", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(10, self.robot.memory)
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, self.robot.ALLOWED_CATEGORIES)
        self.assertEqual([], self.robot.installed_software)

    def test_invalid_category_raise(self):
        with self.assertRaises(Exception) as ex:
            ClimbingRobot("", "TestType", 10, 10)
        self.assertEqual(str(ex.exception), f"Category should be one of {self.robot.ALLOWED_CATEGORIES}")

    def test_get_used_capacity_success(self):
        self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 2,
            'memory_consumption': 1
        })
        self.robot.install_software({
            'name': 'VS Code',
            'capacity_consumption': 3,
            'memory_consumption': 2
        })

        actual = self.robot.get_used_capacity()

        self.assertEqual(5, actual)

    def test_get_available_capacity_success(self):
        self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 2,
            'memory_consumption': 1
        })
        self.robot.install_software({
            'name': 'VS Code',
            'capacity_consumption': 2,
            'memory_consumption': 2
        })

        actual = self.robot.get_available_capacity()

        self.assertEqual(6, actual)

    def test_get_used_memory_success(self):
        self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 2,
            'memory_consumption': 1
        })
        self.robot.install_software({
            'name': 'VS Code',
            'capacity_consumption': 2,
            'memory_consumption': 2
        })

        actual = self.robot.get_used_memory()

        self.assertEqual(3, actual)

    def test_get_available_memory_success(self):
        self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 2,
            'memory_consumption': 1
        })
        self.robot.install_software({
            'name': 'VS Code',
            'capacity_consumption': 2,
            'memory_consumption': 2
        })

        actual = self.robot.get_available_memory()

        self.assertEqual(7, actual)

    def test_install_software_success(self):
        actual = self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 10,
            'memory_consumption': 10
        })

        self.assertEqual("Software 'VS' successfully installed on Mountain part.", actual)
        self.assertEqual([{'capacity_consumption': 10, 'memory_consumption': 10, 'name': 'VS'}], self.robot.installed_software)

    def test_install_software_fail(self):
        actual = self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 11,
            'memory_consumption': 10
        })

        self.assertEqual("Software 'VS' cannot be installed on Mountain part.", actual)
        self.assertEqual([], self.robot.installed_software)

        actual = self.robot.install_software({
            'name': 'VS',
            'capacity_consumption': 10,
            'memory_consumption': 11
        })

        self.assertEqual("Software 'VS' cannot be installed on Mountain part.", actual)
        self.assertEqual([], self.robot.installed_software)