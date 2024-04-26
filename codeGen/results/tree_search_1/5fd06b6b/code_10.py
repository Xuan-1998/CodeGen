# Read the number of days from stdin
n = int(input())

# Read the number of marks above the water level for each day
marks_above = list(map(int, input().split()))

# Initialize the running sum of marks below the water level
sum_below = 0

# Iterate over each day
for i in range(n):
    # Calculate the number of marks below the water level for the current day
    # It's the total number of days so far (i+1) minus the number of marks above
    # and minus 1 for the water level mark itself
    marks_below = (i + 1) - marks_above[i] - 1
    # Add to the running sum
    sum_below += marks_below

# Output the sum of marks below the water level
print(sum_below)
