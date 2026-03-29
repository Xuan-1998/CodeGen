# Step 1: Read the input
n = int(input())
marks_above_water = list(map(int, input().split()))

# Step 2: Initialize a variable to store the minimum sum of marks below water level
min_sum = float('inf')

# Step 3: Iterate over each day and calculate the number of marks below water level
for i in range(1, n):
    marks_below_water = i - marks_above_water[i-1]
    # Update the minimum sum if the current sum is smaller
    min_sum = min(min_sum, marks_below_water)

# Step 4: Print the minimum sum
print(min_sum)
