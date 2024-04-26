def min_sum_marks_below_water(n, marks_above):
    # Initialize the current water level and the sum of marks below the water level
    water_level = 0
    sum_below_water = 0

    # Iterate over each day
    for mark_above in marks_above:
        # Update the water level to be at least as high as the marks above the water level
        water_level = max(water_level, mark_above)
        # Calculate the marks below the water level and add to the sum
        sum_below_water += water_level - mark_above

    return sum_below_water

# Read input from stdin
n = int(input().strip())
marks_above = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_sum_marks_below_water(n, marks_above))
