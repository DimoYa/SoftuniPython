def accommodate(*guest_group, **available_rooms):
    result = {}
    return_str = ""
    rooms = {int(key.replace('room_', '')): value for key, value in available_rooms.items()}
    guests = list(guest_group)
    ordered_rooms = dict(sorted(rooms.items(), key=lambda x: (x[1], x[0])))

    for guest_number in guest_group:
        for room_n, room_c in ordered_rooms.items():
            if guest_number == room_c or room_c > guest_number:
                result[room_n] = guest_number
                del ordered_rooms[room_n]
                guests.remove(guest_number)
                break

    if result:
        return_str += f"A total of {len(result)} accommodations were completed!\n"
        for k, v in sorted(result.items(), key=lambda kvp: kvp[0]):
            return_str += f"<Room {k} accommodates {v} guests>\n"
    else:
        return_str += "No accommodations were completed!\n"
    if guests:
        return_str += f"Guests with no accommodation: {sum(guests)}\n"
    if ordered_rooms:
        return_str += f"Empty rooms: {len(ordered_rooms)}"

    return return_str


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
