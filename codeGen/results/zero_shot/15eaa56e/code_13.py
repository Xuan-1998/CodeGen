import sys

n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

tasks = []
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    tasks.append((l, r))

def is_sorted(subtable):
    for i in range(1, len(subtable)):
        for j in range(m):
            if subtable[i-1][j] > subtable[i][j]:
                return False
    return True

for task in tasks:
    l, r = task
    subtable = [[row[j] for row in rows[l-1:r]] for j in range(m)]
    if is_sorted(subtable):
        print("Yes")
        break
else:
    print("No")
