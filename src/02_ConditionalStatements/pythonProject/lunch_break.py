import math

tv_show_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
break_time = break_duration * 1/4
remaining_time = break_duration - lunch_time - break_time

diff = abs(episode_duration - remaining_time)

if remaining_time >= episode_duration:
    print(f'You have enough time to watch {tv_show_name} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {tv_show_name}, you need {math.ceil(diff)} more minutes.')
    