import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)

k = int(sys.stdin.readline())

sorted_cols = [True] * m  # assume all columns are sorted initially

# Preprocess the table
for i in range(n):
    for j in range(1, m):  # check each cell with its left neighbor
        if table[i][j - 1] > table[i][j]:
            sorted_cols[j - 1] = False  # mark as "not sorted"

# Process tasks
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    for i in range(l - 1, r):  # iterate through rows within task range
        if not all(table[i][j] <= table[i + 1][j] for j in range(m)):
            break
    else:  # all rows in the task range are sorted
        for j in range(m):
            if not sorted_cols[j]:
                break
        else:
            sorted_cols = [True] * m

# Check for sorted columns
for i, is_sorted in enumerate(sorted_cols):
    if is_sorted:
        print("Yes")
        exit(0)

print("No")
