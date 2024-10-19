def gather_credits(number_of_credits, *courses):
    enrollment = {}
    collected_credits = 0
    result = ""

    for name, credit in courses:

        if collected_credits >= number_of_credits:
            break
        if name not in enrollment:
            collected_credits += credit
            enrollment[name] = credit

    if collected_credits >= number_of_credits:
        result += f"Enrollment finished! Maximum credits: {collected_credits}.\n"
        result += f"Courses: {', '.join(sorted(enrollment.keys(), key=lambda x: x[0]))}"
    else:
        result += (f"You need to enroll in more courses!"
                   f" You have to gather {number_of_credits - collected_credits} credits more.")

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

