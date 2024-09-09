courses = {}

students_input = input()

while ":" in students_input:
    name, points, course = students_input.split(":")
    points = int(points)

    if course not in courses:
        courses[course] = []

    courses[course].append(f"{name} - {points}")
    students_input = input()

course_to_print = students_input.replace("_", " ")

if course_to_print in courses:
    print("\n".join(courses[course_to_print]))
