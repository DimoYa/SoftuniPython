import re

force_dict = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        force_side, force_user = line.split(" | ")

        # Check if force_user is already in any side
        user_exists = any(force_user in users for users in force_dict.values())

        if not user_exists:
            # If force_side doesn't exist, create it
            if force_side not in force_dict:
                force_dict[force_side] = []
            # Add the user to the side
            force_dict[force_side].append(force_user)

    elif " -> " in line:
        force_user, force_side = line.split(" -> ")

        # Remove the user from their current side if they exist
        user_found = False
        for side, users in force_dict.items():
            if force_user in users:
                users.remove(force_user)
                user_found = True
                break

        # If the side doesn't exist, create it
        if force_side not in force_dict:
            force_dict[force_side] = []

        # Add the user to the new side
        force_dict[force_side].append(force_user)

        # Print message indicating the user joined the new side
        print(f"{force_user} joins the {force_side} side!")

# Output the results
for side, users in force_dict.items():
    if users:  # Only print if there are users on that side
        print(f"Side: {side}, Members: {len(users)}")
        print("\n".join([f"! {user}" for user in users]))
