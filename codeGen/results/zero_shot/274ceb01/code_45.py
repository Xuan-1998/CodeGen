# Step 1: Read input
n = int(input())
marks_above_water = list(map(int, input().split()))

# Step 2: Initialize minimum sum of marks below water
min_sum = float('inf')

# Step 3: Iterate over each day and calculate sum of marks below water
for i in range(n):
    # Calculate number of marks above water on this day
    marks_above_water_today = marks_above_water[i]

    # Calculate number of marks below water on this day
    marks_below_water_today = i - marks_above_water_today

    # Update minimum sum if necessary
    min_sum = min(min_sum, marks_below_water_today)

# Step 4: Print the minimum possible sum of marks strictly below the water level among all days
print(min_sum)
