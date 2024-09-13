n = int(input())
parking_lot = set()

for _ in range(n):
    command, plate_num = input().split(", ")

    if command == "IN":
        parking_lot.add(plate_num)
    elif command == "OUT":
        parking_lot.remove(plate_num)

if parking_lot:
    for plate in parking_lot:
        print(plate)
else:
    print("Parking Lot is Empty")
