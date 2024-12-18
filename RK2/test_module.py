import unittest
from main_refactor import Department, Faculty, DepartmentFaculty  # Импорт классов
from main_refactor import get_faculty_departments, get_max_students_per_faculty, get_faculty_with_departments  # Импорт функций
class TestDepartmentFacultyFunctions(unittest.TestCase):
    def setUp(self):
        self.deps = [
            Department(1, "FN4", 1894, 4),
            Department(2, "IU7", 1947, 1),
            Department(3, "IU5", 1938, 1),
        ]
        self.facs = [
            Faculty(id=1, name="Engineering"),
            Faculty(id=2, name="Energetic"),
        ]
        self.deps_to_facs = [
            DepartmentFaculty(dep_id=1, fac_id=4),
            DepartmentFaculty(dep_id=2, fac_id=1),
        ]

    def test_get_faculty_departments(self):
        result = get_faculty_departments(self.facs, self.deps, "E")
        self.assertEqual(result, {"Engineering": ["IU7"], "Energetic": []})

    def test_get_max_students_per_faculty(self):
        result = get_max_students_per_faculty(self.facs, self.deps)
        expected = [("Engineering", ("IU7", 1947))]
        self.assertEqual(result, expected)

    def test_get_faculty_with_departments(self):
        result = get_faculty_with_departments(self.facs, self.deps, self.deps_to_facs)
        expected = {
            "Engineering": [(1947, "IU7", "Engineering")],
            "Energetic": [],
        }
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
