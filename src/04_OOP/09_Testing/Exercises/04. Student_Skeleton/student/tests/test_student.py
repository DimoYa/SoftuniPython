from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    dict = {"Python": ["n1", "n2", "n3"], "Java": ["n1"]}

    def setUp(self):
        self.student1 = Student("std1", self.dict)
        self.student2 = Student("std2")

    def test_init(self):
        self.assertEqual("std1", self.student1.name)
        self.assertEqual(self.dict, self.student1.courses)
        self.assertEqual("std2", self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_enroll_existing_course(self):
        # Act
        result = self.student1.enroll("Java", ["n2", "n3"])
        # Assert
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['n1', 'n2', 'n3'], self.student1.courses["Java"])

    def test_enroll_new_course(self):
        # Act
        result = self.student1.enroll("c#",["n4", "n5"], "Y")
        # Assert
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n4", "n5"], self.student1.courses["c#"])

        # Act
        result = self.student1.enroll("js",["n4", "n5"], "")
        # Assert
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n4", "n5"], self.student1.courses["js"])

    def test_enroll_new_course_no_notes(self):
        # Act
        result = self.student2.enroll("c#", ["n4", "n5"], "N")
        # Assert
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student2.courses["c#"])

    def test_add_notes_course_notfound_raise(self):
        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("c#", ["n4", "n5"])
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_add_notes(self):
        # Act
        result = self.student1.add_notes("Python", "n4")
        # Assert
        self.assertEqual("Notes have been updated", result)
        self.assertIn("n4", self.student1.courses["Python"])

    def test_leave_course_notfound_raise(self):
        # Act and Assert
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("c#")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_leave_course(self):
        # Act
        result = self.student1.leave_course("Python")
        # Assert
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student1.courses)


if __name__ == "__main__":
    main()
