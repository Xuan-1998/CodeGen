# Read input
n = int(input())
marks_above = list(map(int, input().split()))

# Initialize variables
highest_level = 0
sum_below = 0

# Calculate the minimum possible sum of the number of marks below the water level
for m in marks_above:
    highest_level = max(highest_level, m + 1)
    sum_below += highest_level - (m + 1)

# Output the result
print(sum_below)
