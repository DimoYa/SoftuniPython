class PianoPiece:
    def __init__(self, piece, composer, key):
        self.piece = piece
        self.composer = composer
        self.key = key

integer = int(input())

pieces = {}
result = []

for _ in range(integer):
    p, c, k = input().split("|")
    piano_piece = PianoPiece(p, c, k)
    pieces[p] = piano_piece

command = input()


def add_command(dictionary, params):
    p, c, k = params

    if p in dictionary:
        result.append(f"{p} is already in the collection!")
    else:
        result.append(f"{p} by {c} in {k} added to the collection!")
        current_piece = PianoPiece(p, c, k)
        dictionary[p] = current_piece

    return dictionary


def remove_command(dictionary, params):
    p = params[0]
    if p in dictionary:
        result.append(f"Successfully removed {p}!")
        del dictionary[p]
    else:
        result.append(f"Invalid operation! {p} does not exist in the collection.")

    return dictionary


def change_key_command(dictionary, params):
    p, new_k = params

    if p in dictionary:
        result.append(f"Changed the key of {p} to {new_k}!")
        current_piece = dictionary[p]
        current_piece.key = new_k
    else:
        result.append(f"Invalid operation! {p} does not exist in the collection.")

    return dictionary


while not command == "Stop":
    token = command.split("|")
    command_name = token[0]
    command_params = token[1:]

    if command_name == "Add":
        add_command(pieces, command_params)
    elif command_name == "Remove":
        remove_command(pieces, command_params)
    elif command_name == "ChangeKey":
        change_key_command(pieces, command_params)

    command = input()

print("\n".join(result), end="\n")
for key, value in pieces.items():
    print(f"{key} -> Composer: {value.composer}, Key: {value.key}")