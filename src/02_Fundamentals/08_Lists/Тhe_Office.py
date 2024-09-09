happiness = [int(h) for h in input().split()]
factor = int(input())

multiplied_happiness = [h * factor for h in happiness]

avg_factor = sum(multiplied_happiness) / len(multiplied_happiness)

half_of_the_employees = len(happiness) / 2

happy_employees = [e for e in multiplied_happiness if e >= avg_factor]

if len(happy_employees) >= half_of_the_employees:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!")
