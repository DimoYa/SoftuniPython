from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(TestCase):
    SOFTWARE = {'name': 'Example Software', 'capacity_consumption': 1, 'memory_consumption': 1}

    def setUp(self):
        self.robot = ClimbingRobot("Alpine", "Part", 10, 20)
        self.robot.installed_software.append(self.SOFTWARE)

    def test_init(self):
        expected = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("Part", self.robot.part_type)
        self.assertEqual(10, self.robot.capacity)
        self.assertEqual(20, self.robot.memory)
        self.assertEqual([self.SOFTWARE], self.robot.installed_software)
        self.assertEqual(expected, self.robot.ALLOWED_CATEGORIES)

    def test_invalid_category_raise(self):
        with self.assertRaises(Exception) as ex:
            ClimbingRobot("Invalid", "Part", 10, 20)
        self.assertEqual(str(ex.exception), f"Category should be one of {self.robot.ALLOWED_CATEGORIES}")

    def test_get_used_capacity(self):
        software = {'name': 'Example Software2', 'capacity_consumption': 3, 'memory_consumption': 2}
        self.robot.install_software(software)
        result = self.robot.get_used_capacity()
        self.assertEqual(4, result)

    def test_get_available_capacity(self):
        software = {'name': 'Example Software2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.robot.install_software(software)
        result = self.robot.get_available_capacity()
        self.assertEqual(8, result)
        self.assertEqual(10, self.robot.capacity)

    def test_get_used_memory(self):
        software = {'name': 'Example Software2', 'capacity_consumption': 3, 'memory_consumption': 2}
        self.robot.install_software(software)
        result = self.robot.get_used_memory()
        self.assertEqual(3, result)

    def test_get_available_memory(self):
        software = {'name': 'Example Software2', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.robot.install_software(software)
        result = self.robot.get_available_memory()
        self.assertEqual(18, result)
        self.assertEqual(20, self.robot.memory)

    def test_install_software_success(self):
        software = {'name': 'Example Software', 'capacity_consumption': 1, 'memory_consumption': 1}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Example Software' successfully installed on {self.robot.category} part.", result)

    def test_install_software_cannot_capacity(self):
        software = {'name': 'Example Software', 'capacity_consumption': 11, 'memory_consumption': 1}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Example Software' cannot be installed on {self.robot.category} part.", result)

        software = {'name': 'Example Software', 'capacity_consumption': 10, 'memory_consumption': 1}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Example Software' cannot be installed on {self.robot.category} part.", result)

    def test_install_software_cannot_memory(self):
        software = {'name': 'Example Software', 'capacity_consumption': 9, 'memory_consumption': 21}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Example Software' cannot be installed on {self.robot.category} part.", result)

        software = {'name': 'Example Software', 'capacity_consumption': 9, 'memory_consumption': 20}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Example Software' cannot be installed on {self.robot.category} part.", result)

    def test_no_installed_software(self):
        self.robot.installed_software = []
        self.assertEqual(0, self.robot.get_used_capacity())
        self.assertEqual(self.robot.capacity, self.robot.get_available_capacity())
        self.assertEqual(0, self.robot.get_used_memory())
        self.assertEqual(self.robot.memory, self.robot.get_available_memory())

    def test_install_duplicate_software(self):
        result = self.robot.install_software(self.SOFTWARE)
        self.assertEqual(f"Software '{self.SOFTWARE['name']}' successfully installed on {self.robot.category} part.", result)
        self.assertEqual(2, len(self.robot.installed_software))  # Assuming duplicates are allowed

    def test_install_software_exact_resources(self):
        software = {'name': 'Exact Fit', 'capacity_consumption': self.robot.get_available_capacity(), 'memory_consumption': self.robot.get_available_memory()}
        result = self.robot.install_software(software)
        self.assertEqual(f"Software 'Exact Fit' successfully installed on {self.robot.category} part.", result)
        self.assertEqual(0, self.robot.get_available_capacity())
        self.assertEqual(0, self.robot.get_available_memory())

    def test_invalid_software_format(self):
        with self.assertRaises(KeyError):
            self.robot.install_software({'capacity_consumption': 1})  # Missing 'name' and 'memory_consumption'


if __name__ == "__main__":
    main()
