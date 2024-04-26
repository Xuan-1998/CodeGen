# Receive the number of days from stdin
n = int(input())

# Receive the number of marks strictly above the water level on each day
marks_above = list(map(int, input().split()))

# Initialize the minimum sum of marks below the water level
min_sum_below = 0

# Initialize the current water level to 0
current_water_level = 0

for i in range(n):
    # The water level must be at least as high as the highest number of marks above it seen so far
    current_water_level = max(current_water_level, marks_above[i])

    # Add the number of marks below the water level for the current day to the total sum
    min_sum_below += i - current_water_level

# Output the minimum possible sum of the number of marks strictly below the water level
print(min_sum_below)
