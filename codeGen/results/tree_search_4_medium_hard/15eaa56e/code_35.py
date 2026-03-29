import sys

# Input variables
n, m = map(int, input().split())
k = int(input())

# Initialize dictionary to store maximum values for each column
max_values = {}

# Iterate over each row in the subtable
for _ in range(n):
    row = list(map(int, input().split()))
    # Update maximum values for each column
    for col, val in enumerate(row):
        if col not in max_values:
            max_values[col] = val
        else:
            max_values[col] = max(max_values[col], val)

# Initialize answer
is_sorted = "Yes"

# Iterate over the columns
for col in range(m):
    # Check if the column is sorted
    if row == sorted(row):
        is_sorted = "No"
        break

print(is_sorted)
