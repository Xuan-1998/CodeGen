# Read in the number of days
n = int(input())

# Read in the number of marks above the water level for each day
marks_above = list(map(int, input().split()))

# Initialize variables
max_height = 0
sum_below = 0

# Iterate over each day
for i in range(n):
    # Calculate the highest possible mark for the current day
    possible_height = max_height + 1 if max_height + 1 <= marks_above[i] else marks_above[i]
    # Update the maximum height
    max_height = max(max_height, possible_height)
    # Update the sum of marks below the water level
    sum_below += i - max_height

# Output the sum of marks below the water level
print(sum_below)
