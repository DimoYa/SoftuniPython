def softuni_students(*students, **courses):
    successful = {}
    unsuccessful = []
    result = ''

    for course_id, student_name in students:
        if course_id in courses:
            successful[student_name] = courses.get(course_id)
        else:
            unsuccessful.append(student_name)

    if successful:
        for student_name, course_name in sorted(successful.items(), key=lambda x: (x[0])):
            result += f"*** A student with the username {student_name} has successfully finished the course {course_name}!\n"

    if unsuccessful:
        result += f"!!! Invalid course students: {', '.join(sorted(unsuccessful))}"

    return result.strip()


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))