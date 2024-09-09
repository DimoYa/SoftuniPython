def register_user(parking, parameters):
    user = parameters[0]
    plate_num = parameters[1]

    if user in parking:
        print(f"ERROR: already registered with plate number {plate_num}")
    else:
        parking[user] = plate_num
        print(f"{user} registered {plate_num} successfully")
    return parking


def unregister_user(parking, parameters):
    user = parameters[0]

    if user not in parking:
        print(f"ERROR: user {user} not found")
    else:
        del parking[user]
        print(f"{user} unregistered successfully")
    return parking


n = int(input())
parking = {}

for _ in range(n):
    line = input().split()
    command = line[0]
    parameters = line[1:]

    if command == "register":
        parking = register_user(parking, parameters)
    elif command == "unregister":
        parking = unregister_user(parking, parameters)

for user, plate in parking.items():
    print(f"{user} => {plate}")
