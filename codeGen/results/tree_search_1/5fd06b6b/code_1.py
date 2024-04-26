# Read input from stdin
n = int(input())
m = list(map(int, input().split()))

# Initialize variables
water_level = 0
total_marks_below = 0

# Process each day
for mi in m:
    # The water level for the current day is the maximum of the previous water level
    # and mi + 1 to ensure mi marks above the water level
    water_level = max(water_level, mi + 1)
    # Add the difference between the current water level and mi (marks above)
    # to get the marks below for the current day
    total_marks_below += water_level - mi - 1

# Print the total minimum sum of marks below the water level
print(total_marks_below)
