budget = float(input())
season = input()
destination = ''
accommodation = ''

if budget <= 100:
    destination = 'Somewhere in Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        budget *= 0.3
    else:
        accommodation = 'Hotel'
        budget *= 0.7
elif 100 < budget <= 1000:
    destination = 'Somewhere in Balkans'
    if season == 'summer':
        accommodation = 'Camp'
        budget *= 0.4
    else:
        accommodation = 'Hotel'
        budget *= 0.8
else:
    destination = 'Somewhere in Europe'
    accommodation = 'Hotel'
    budget *= 0.9

print(destination)
print(f'{accommodation} - {budget:.2f}')
