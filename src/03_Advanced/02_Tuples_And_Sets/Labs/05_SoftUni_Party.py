n = int(input())
guests = set()

for _ in range(n):
    guests.add(input())

reservation_code = input()

while reservation_code != "END":
    guests.remove(reservation_code)
    reservation_code = input()

print(len(guests))
for guest in sorted(guests):
    print(guest)
