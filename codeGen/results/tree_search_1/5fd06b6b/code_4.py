def min_marks_below_water(n, marks_above):
    # Initialize the water level on the first day
    water_level = marks_above[0] + 1
    # Initialize the sum of marks below the water level
    sum_below = 0

    # Iterate over the days
    for i in range(1, n):
        # The water level for the current day is the maximum of the water level
        # needed to keep mi marks above and the water level of the previous day
        water_level = max(water_level, marks_above[i] + 1)
        # Add the number of marks below the water level for the current day
        sum_below += i - marks_above[i]

    # Add the number of marks below the water level for the first day
    sum_below += 0  # Since there are no marks below on the first day

    return sum_below

# Read input from stdin
n = int(input().strip())
marks_above = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_marks_below_water(n, marks_above))
