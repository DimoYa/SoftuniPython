from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:
            album = [a for a in self.albums if a.name == album_name][0]
            if album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album_name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self):
        result = ""
        result += f"Band {self.name}\n"
        for a in self.albums:
            result += f"{a.details()}"

        return result.strip()
