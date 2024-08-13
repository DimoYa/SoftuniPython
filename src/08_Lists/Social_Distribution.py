population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())
is_possible = True
processed_index = 0

if sum(population) < len(population) * minimum_wealth:
    is_possible = False

for i in range(len(population)):
    if not is_possible:
        break
    wealthiest = max(population)
    wealthiest_index = population.index(wealthiest)
    if population[i] < minimum_wealth:
        diff = minimum_wealth - population[i]
        population[wealthiest_index] -= diff
        population[i] += diff
        processed_index = i

if is_possible:
    print(population)
else:
    print("No equal distribution possible")