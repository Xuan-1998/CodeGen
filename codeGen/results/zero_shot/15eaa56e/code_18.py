import sys

# Read the table
n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)

# Read the tasks
k = int(sys.stdin.readline())
tasks = []
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    tasks.append((l, r))

def is_sorted(lst):
    return lst == sorted(lst)

for l, r in tasks:
    for col in range(m):
        subtable = [row[col] for row in table[l-1:r]]
        if not is_sorted(subtable):
            print("No")
            break
    else:
        print("Yes")
