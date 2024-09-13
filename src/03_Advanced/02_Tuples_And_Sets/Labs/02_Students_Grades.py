n = int(input())
students = {}

for _ in range(n):
    name, grade_value = tuple(input().split())
    grade_value = float(grade_value)

    if name not in students:
        students[name] = []
    students[name].append(grade_value)

for name, values in students.items():
    avg = sum(values) / len(values)
    print(f"{name} -> {' '.join([f'{item:.2f}' for item in values])} (avg: {avg:.2f})")
