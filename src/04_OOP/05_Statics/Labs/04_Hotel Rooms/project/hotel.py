from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room is not None:
            room.take_room(people)

    def free_room(self, room_number):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room is not None:
            room.free_room()

    def status(self):
        result = ""
        result += f"Hotel {self.name} has {sum([r.guests for r in self.rooms])} total guests\n"
        result += f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}\n"

        return result


