import math

time_first = int(input())
second_first = int(input())
third_first = int(input())

sum_of_seconds = time_first + second_first + third_first

minutes = sum_of_seconds // 60
seconds = sum_of_seconds % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
