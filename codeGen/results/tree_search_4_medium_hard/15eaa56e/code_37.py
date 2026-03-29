import sys

# Input: The input consists of a table of integers, the number of rows and columns, and a set of tasks consisting of subtable indices.
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# Task: Determine if the subtable is sorted in non-decreasing order in at least one column.
max_values = {}
for row in table:
    for col, val in enumerate(row):
        max_values[col] = max(max_values.get(col, 0), val)

def is_subtable_sorted(l, r):
    for i in range(m):
        prev_val = -1
        for j in range(l-1, r+1):
            if table[j][i] > prev_val:
                return False
            prev_val = table[j][i]
    return True

for task in [list(map(int, input().split())) for _ in range(k)]:
    l, r = task
    if is_subtable_sorted(l-1, r):
        print("Yes")
        sys.exit()
print("No")
