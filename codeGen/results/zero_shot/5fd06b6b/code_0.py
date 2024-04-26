# Read the input
n = int(input().strip())
marks_above_water = list(map(int, input().strip().split()))

# Initialize variables
below_water_total = 0
current_level = 0

# Process each day
for i in range(n):
    # If current level is greater than the marks above water, adjust the level
    if current_level > marks_above_water[i]:
        below_water_total += current_level - marks_above_water[i]
        current_level = marks_above_water[i]
    # Increase the current level for the next day
    current_level += 1

# Output the result
print(below_water_total)
