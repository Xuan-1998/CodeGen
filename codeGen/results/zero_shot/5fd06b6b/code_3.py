def find_min_sum_below_water(n, marks_above):
    # Initialize the sum of marks below the water level
    sum_below_water = 0
    # Initialize the highest water level used so far
    highest_mark_used = 0

    for mi in marks_above:
        # The water level for the current day is the next highest mark not used
        # which is one more than the highest mark used so far
        water_level = highest_mark_used + 1
        # Calculate the number of marks below the water level for the current day
        marks_below = water_level - 1 - mi
        sum_below_water += marks_below
        # Update the highest mark used if the current water level is higher
        highest_mark_used = max(highest_mark_used, water_level)

    return sum_below_water

# Read input from stdin
n = int(input().strip())
marks_above = list(map(int, input().strip().split()))

# Get the result and print it
result = find_min_sum_below_water(n, marks_above)
print(result)
