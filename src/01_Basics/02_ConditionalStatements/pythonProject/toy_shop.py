import math

puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
small_truck = 2


cost_of_excursion = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_small_trucks = int(input())


sum_total = (
        num_puzzles * puzzle + num_talking_dolls * talking_doll
        + num_teddy_bears * teddy_bear + num_minions * minion + num_small_trucks * small_truck)

count_toys = num_puzzles + num_talking_dolls + num_teddy_bears + num_minions + num_small_trucks

if count_toys >= 50:
    sum_total *= 0.75

sum_after_rent = sum_total * 0.9

diff = abs(sum_after_rent - cost_of_excursion)

if sum_after_rent >= cost_of_excursion:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
