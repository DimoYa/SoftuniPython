class Piece:

    def __init__(self, piece_name, composer, key):
        self.piece_name = piece_name
        self.composer = composer
        self.key = key


n = int(input())
pieces = {}

for _ in range(n):
    piece_name, composer, key = input().split("|")
    piece = Piece(piece_name, composer, key)
    pieces[piece_name] = piece

command = input()


def add_command(params, pieces_dict):
    name, c, k = params

    if name in pieces_dict:
        print(f"{name} is already in the collection!")
    else:
        print(f"{name} by {c} in {k} added to the collection!")
        pieces_dict[name] = Piece(name, c, k)
    return pieces_dict


def remove_command(params, pieces_dict):
    name = params[0]

    if name not in pieces_dict:
        print(f"Invalid operation! {name} does not exist in the collection.")
    else:
        print(f"Successfully removed {name}!")
        del pieces_dict[name]
    return pieces_dict


def change_key_command(params, pieces_dict):
    name, new_key = params

    if name not in pieces_dict:
        print(f"Invalid operation! {name} does not exist in the collection.")
    else:
        print(f"Changed the key of {name} to {new_key}!")
        pieces_dict[name].key = new_key
    return pieces_dict


while not command == "Stop":
    token = command.split("|")
    command_name = token[0]
    command_params = token[1:]

    if command_name == "Add":
        pieces = add_command(command_params, pieces)
    if command_name == "Remove":
        pieces = remove_command(command_params, pieces)
    if command_name == "ChangeKey":
        pieces = change_key_command(command_params, pieces)

    command = input()

for key, value in pieces.items():
    print(f"{value.piece_name} -> Composer: {value.composer}, Key: {value.key}")
