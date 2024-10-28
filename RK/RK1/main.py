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
        return (self.name<obj.name)

class DemartmentFaculty:
    
    def __init__(self, dep_id, fac_id):

        self.dep_id = dep_id 
        self.fac_id = fac_id 

deps = [
    Department(1, "FN4", 1894, 4),
    Department(2, "IU7", 1947, 1),
    Department(3, "IU5", 1938, 1),
    Department(4, "Э6", 1954, 5),
    Department(5, "MT3", 1949, 2),
    Department(6, "MT4", 2045, 2),
    Department(7, "FN2", 1843, 4),
    Department(8, "RK1", 1932, 2)
]

facs = [
    Faculty(id=1, name="Computer science"),
    Faculty(id=2, name="Engineering"),
    Faculty(id=3, name="Business IT"),
    Faculty(id=4, name="Physics"),
    Faculty(id=5, name="Energetic")
]


deps_to_facs = [
    DemartmentFaculty(dep_id=1, fac_id=4),
    DemartmentFaculty(dep_id=2, fac_id=1),
    DemartmentFaculty(dep_id=3, fac_id=1),
    DemartmentFaculty(dep_id=4, fac_id=5),
    DemartmentFaculty(dep_id=5, fac_id=2),
    DemartmentFaculty(dep_id=6, fac_id=2),
    DemartmentFaculty(dep_id=7, fac_id=4),
    DemartmentFaculty(dep_id=8, fac_id=2)
    
]

def main():
    
    print("Здание №1")
    dict1 = {}
    
    for fac in facs:
        if (fac.name.startswith("E")):
            dict1[fac.name] = [depart.name for depart in deps if depart.faculty_id == fac.id]
    print(dict1)

    print("Здание №2")
    dict2 = {}
    for fac in facs:
        depts = [dept for dept in deps if dept.faculty_id == fac.id]
        if(len(depts)!=0):
            max_dept = max(depts, key=lambda d: d.students)
            dict2[fac.name] = (max_dept.name, max_dept.students)
    print(sorted(dict2.items(), key=lambda d: d[1][1], reverse=True))

    print("Здание №3")
    dict3 = {}
    many_to_many_temp = [(f.name, d.fac_id, d.dep_id) 
        for f in facs
        for d in deps_to_facs 
        if f.id==d.fac_id]
    many_to_many = [(d.students, d.name, name) 
        for name, fac_id, dep_id in many_to_many_temp
        for d in deps if d.id==dep_id]
   
    for sup in sorted(facs):
        dict3[sup.name] = list(filter(lambda i: i[2] == sup.name, many_to_many))
    print(dict3)

if __name__ == "__main__":
    main()