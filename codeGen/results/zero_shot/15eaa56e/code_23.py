import sys

n, m = map(int, input().split())
table = [[int(x) for x in input().split()] for _ in range(n)]

k = int(input())

for l, r in [tuple(map(int, input().split())) for _ in range(k)]:
    # Check if the subtable is sorted in at least one column
    for j in range(m):
        if not all(table[i][j] <= table[i+1][j] for i in range(l-1, r)):
            print("No")
            sys.exit()
print("Yes")
