def min_marks_below_water(n, marks_above):
    # Initialize the highest water level to 0
    highest_water_level = 0
    # Initialize the sum of marks below the water level to 0
    sum_below = 0

    for i in range(n):
        # Calculate the potential new water level
        potential_water_level = marks_above[i] + 1
        # Update the highest water level if the new level is higher
        highest_water_level = max(highest_water_level, potential_water_level)
        # Add the number of marks below the water level to the sum
        sum_below += highest_water_level - marks_above[i] - 1

    return sum_below

# Read input from stdin
n = int(input())
marks_above = list(map(int, input().split()))

# Get the result and print it to stdout
print(min_marks_below_water(n, marks_above))
