width = int(input())
length = int(input())
height = int(input())

total_space_volume = width * length * height
is_enough = True

used_volume = 0

while True:
    command = input().strip()
    if command.lower() == 'done':
        break
    used_volume += int(command)

    if used_volume >= total_space_volume:
        is_enough = False
        break

diff = abs(total_space_volume - used_volume)

if is_enough:
    print(f'{diff} Cubic meters left.')
else:
    print(f'No more free space! You need {diff} Cubic meters more.')
