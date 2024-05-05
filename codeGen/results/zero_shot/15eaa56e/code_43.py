import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)

k = int(sys.stdin.readline())

# Process each task to check if the subtable is sorted
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    subtable = [row[l-1:r] for row in table[l-1:r]]
    
    # Check if the subtable is sorted in non-decreasing order
    if any(row[i] > row[i+1] for row in subtable for i in range(len(row)-1)):
        print("No")
    else:
        print("Yes")
