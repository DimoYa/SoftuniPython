from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs: list[Song] = list(songs)

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            song = [s for s in self.songs if s.name == song_name][0]
            if self.published:
                return "Cannot remove songs. Album is published."
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = ""
        result += f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result.strip()

