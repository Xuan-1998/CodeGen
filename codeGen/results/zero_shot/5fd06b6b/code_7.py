# Read the number of days
n = int(input())

# Read the number of marks strictly above the water level for each day
marks_above = list(map(int, input().split()))

# Initialize the sum of marks below the water level
sum_below = 0

# Calculate the sum of marks below the water level for each day
for i in range(1, n + 1):
    sum_below += i - 1 - marks_above[i - 1]

# Output the result
print(sum_below)
