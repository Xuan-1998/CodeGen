import sys

# Read inputs from stdin
n, m = map(int, input().split())
k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

# Initialize the table
table = [[0 for _ in range(m)] for _ in range(n)]

# Read the table from stdin
for i in range(n):
    row = list(map(int, input().split()))
    table[i] = row

# Check if the subtable is sorted in non-decreasing order in at least one column
def is_sorted(subtable):
    for j in range(len(subtable[0])):
        if not all(subtable[i][j] <= subtable[i+1][j] for i in range(len(subtable)-1)):
            return False
    return True

# Iterate over tasks and check if the subtable is sorted in at least one column
for l, r in tasks:
    subtable = [row[l:r+1] for row in table]
    if any(is_sorted(column) for column in zip(*subtable)):
        print("Yes")
        break
else:
    print("No")
