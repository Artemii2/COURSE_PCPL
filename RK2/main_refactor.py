class Department:
    def __init__(self, id, name, students, faculty_id):
        self.id = id
        self.name = name
        self.students = students
        self.faculty_id = faculty_id


class Faculty:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __lt__(self, obj):
        return self.name < obj.name


class DepartmentFaculty:
    def __init__(self, dep_id, fac_id):
        self.dep_id = dep_id
        self.fac_id = fac_id


# Данные
deps = [
    Department(1, "FN4", 1894, 4),
    Department(2, "IU7", 1947, 1),
    Department(3, "IU5", 1938, 1),
    Department(4, "Э6", 1954, 5),
    Department(5, "MT3", 1949, 2),
    Department(6, "MT4", 2045, 2),
    Department(7, "FN2", 1843, 4),
    Department(8, "RK1", 1932, 2),
]

facs = [
    Faculty(id=1, name="Computer science"),
    Faculty(id=2, name="Engineering"),
    Faculty(id=3, name="Business IT"),
    Faculty(id=4, name="Physics"),
    Faculty(id=5, name="Energetic"),
]

deps_to_facs = [
    DepartmentFaculty(dep_id=1, fac_id=4),
    DepartmentFaculty(dep_id=2, fac_id=1),
    DepartmentFaculty(dep_id=3, fac_id=1),
    DepartmentFaculty(dep_id=4, fac_id=5),
    DepartmentFaculty(dep_id=5, fac_id=2),
    DepartmentFaculty(dep_id=6, fac_id=2),
    DepartmentFaculty(dep_id=7, fac_id=4),
    DepartmentFaculty(dep_id=8, fac_id=2),
]


# Функции для здания №1
def get_faculty_departments(faculties, departments, prefix):
    result = {}
    for fac in faculties:
        if fac.name.startswith(prefix):
            result[fac.name] = [dep.name for dep in departments if dep.faculty_id == fac.id]
    return result


# Функция для здания №2
def get_max_students_per_faculty(faculties, departments):
    result = {}
    for fac in faculties:
        depts = [dept for dept in departments if dept.faculty_id == fac.id]
        if depts:
            max_dept = max(depts, key=lambda d: d.students)
            result[fac.name] = (max_dept.name, max_dept.students)
    return sorted(result.items(), key=lambda d: d[1][1], reverse=True)


# Функция для здания №3
def get_faculty_with_departments(faculties, departments, deps_to_facs):
    many_to_many_temp = [
        (f.name, d.fac_id, d.dep_id) for f in faculties for d in deps_to_facs if f.id == d.fac_id
    ]
    many_to_many = [
        (d.students, d.name, name)
        for name, fac_id, dep_id in many_to_many_temp
        for d in departments
        if d.id == dep_id
    ]

    result = {}
    for fac in sorted(faculties):
        result[fac.name] = list(filter(lambda i: i[2] == fac.name, many_to_many))
    return result


# Основная функция
def main():
    print("Здание №1")
    print(get_faculty_departments(facs, deps, "E"))

    print("Здание №2")
    print(get_max_students_per_faculty(facs, deps))

    print("Здание №3")
    print(get_faculty_with_departments(facs, deps, deps_to_facs))


if __name__ == "__main__":
    main()
