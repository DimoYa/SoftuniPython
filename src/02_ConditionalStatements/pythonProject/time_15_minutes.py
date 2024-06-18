hour = int(input())
minutes = int(input())

after_fifteen_minutes = 15

minutes += after_fifteen_minutes

if minutes >= 60 and hour+1 < 24:
    hour += 1
    minutes = minutes - 60
elif minutes >= 60 and hour == 24:
    hour = 1
    minutes = minutes - 60
elif minutes >= 60 and hour == 23:
    hour = 0
    minutes = minutes - 60

if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
