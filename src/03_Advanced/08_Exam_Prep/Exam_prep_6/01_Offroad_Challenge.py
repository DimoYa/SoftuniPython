from collections import deque

# Input for fuel, consumption, and amount of fuel needed
initial_fuel_stack = [int(el) for el in input().split()]
consumption_index = deque([int(el) for el in input().split()])
amount_of_fuel_needed = deque([int(el) for el in input().split()])

reached_altitudes = 0

# Loop until we run out of fuel, consumption indices, or necessary fuel values
while initial_fuel_stack and consumption_index and amount_of_fuel_needed:
    current_fuel = initial_fuel_stack.pop()  # Take the last fuel
    current_consumption = consumption_index.popleft()  # Take the first consumption index
    fuel_remaining = current_fuel - current_consumption  # Calculate the remaining fuel after consumption

    # Check if the remaining fuel is sufficient to reach the corresponding altitude
    if fuel_remaining >= amount_of_fuel_needed[0]:
        amount_of_fuel_needed.popleft()  # Remove the amount of fuel needed for this altitude
        reached_altitudes += 1
        print(f"John has reached: Altitude {reached_altitudes}")
    else:
        # If fuel is insufficient, output failure and break the loop
        print(f"John did not reach: Altitude {reached_altitudes + 1}")
        break

# Check final outcomes based on the number of altitudes reached
if reached_altitudes and amount_of_fuel_needed:  # John failed but reached some altitudes
    result = "John failed to reach the top.\nReached altitudes: "
    for index in range(1, reached_altitudes + 1):
        result += f"Altitude {index}"
        if index != reached_altitudes:
            result += ", "
    print(result)
elif not reached_altitudes:  # John didn't reach any altitudes
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:  # John reached all the altitudes
    print("John has reached all the altitudes and managed to reach the top!")
