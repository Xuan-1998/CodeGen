import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l-1, r-1))

def is_sorted(subtable):
    for i in range(1, m):
        if subtable[0][i] < subtable[0][i-1]:
            return False
    return True

for l, r in tasks:
    subtable = [row[l:r+1] for row in table]
    if is_sorted(subtable):
        print("Yes")
        sys.exit()
print("No")
