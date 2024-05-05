import sys

# Read input table of integers
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# Read number of tasks (k)
k = int(input())

# Process each task
for l, r in [map(int, input().split()) for _ in range(k)]:
    # Check if subtable is sorted in at least one column
    sorted_in_column = False
    for j in range(m):
        column = [row[j] for row in table[l-1:r]]
        if all(column[i] <= column[i+1] for i in range(len(column)-1)):
            sorted_in_column = True
            break

    # Print output
    print("Yes" if sorted_in_column else "No")
