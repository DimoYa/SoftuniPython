groups = int(input())

musala_group = 0
montblanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_tourists = 0

for _ in range(groups):
    current_group = int(input())
    if current_group <= 5:
        musala_group += current_group
    elif 6 <= current_group <= 12:
        montblanc_group += current_group
    elif 13 <= current_group <= 25:
        kilimanjaro_group += current_group
    elif 26 <= current_group <= 40:
        k2_group += current_group
    else:
        everest_group += current_group
    total_tourists += current_group

print(f'{musala_group / total_tourists * 100:.2f}%')
print(f'{montblanc_group / total_tourists * 100:.2f}%')
print(f'{kilimanjaro_group / total_tourists * 100:.2f}%')
print(f'{k2_group / total_tourists * 100:.2f}%')
print(f'{everest_group / total_tourists * 100:.2f}%')
