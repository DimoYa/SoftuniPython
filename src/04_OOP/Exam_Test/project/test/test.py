from unittest import TestCase, main

from project.senior_student import SeniorStudent


class SeniorStudentTest(TestCase):
    def setUp(self):
        self.student = SeniorStudent("1111", "Student1", 2.0)

    def test_init(self):
        self.assertEqual("1111", self.student.student_id)
        self.assertEqual("Student1", self.student.name)
        self.assertEqual(2.0, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_invalid_student_id_raise(self):
        with self.assertRaises(Exception) as ex:
            SeniorStudent("111", "Student1", 2.0)
        self.assertEqual(str(ex.exception), "Student ID must be at least 4 digits long!")

    def test_invalid_student_name_raise(self):
        with self.assertRaises(Exception) as ex:
            SeniorStudent("1111", " ", 2.0)
        self.assertEqual(str(ex.exception), "Student name cannot be null or empty!")

        with self.assertRaises(Exception) as ex:
            SeniorStudent("1111", "", 2.0)
        self.assertEqual(str(ex.exception), "Student name cannot be null or empty!")

    def test_invalid_student_gpa_raise(self):
        with self.assertRaises(Exception) as ex:
            SeniorStudent("1111", "Student", 1.0)
        self.assertEqual(str(ex.exception), "Student GPA must be more than 1.0!")

        with self.assertRaises(Exception) as ex:
            SeniorStudent("1111", "Student", 0)
        self.assertEqual(str(ex.exception), "Student GPA must be more than 1.0!")

    def test_apply_failed(self):
        actual = self.student.apply_to_college(3, "Softuni")

        self.assertEqual("Application failed!", actual)

    def test_apply_success(self):
        actual = self.student.apply_to_college(2, "Softuni")

        self.assertEqual("Student1 successfully applied to Softuni.", actual)
        self.assertEqual({'SOFTUNI'}, self.student.colleges)

    def test_update_failed(self):
        actual = self.student.update_gpa(1)

        self.assertEqual("The GPA has not been changed!", actual)
        self.assertEqual(2.0, self.student.student_gpa)

    def test_update_success(self):
        actual = self.student.update_gpa(3)

        self.assertEqual("Student GPA was successfully updated.", actual)
        self.assertEqual(3.0, self.student.student_gpa)

    def test_self_eq_other(self):
        other = SeniorStudent("1111", "Student2", 2.0)

        result = other == self.student

        self.assertTrue(result)

    def test_self_not_eq_other(self):
        other = SeniorStudent("1111", "Student2", 3.0)

        result = other == self.student

        self.assertFalse(result)


if __name__ == "__main__":
    main()
