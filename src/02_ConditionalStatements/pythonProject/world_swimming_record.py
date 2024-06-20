import math

record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())

seconds = distance_meters * time_per_meter
additional_seconds = math.floor(distance_meters / 15) * 12.5
total_seconds = seconds + additional_seconds

diff = abs(total_seconds - record_seconds)

if total_seconds < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
