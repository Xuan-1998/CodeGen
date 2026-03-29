import sys

# Read input
n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)

k = int(sys.stdin.readline())

for l, r in [map(int, sys.stdin.readline().split()) for _ in range(k)]:
    for j in range(m):  # Check each column
        is_sorted = True
        for i in range(l-1, r):
            if table[i][j] > table[i+1][j]:
                is_sorted = False
                break
        if is_sorted:
            print("Yes")
            sys.exit()
    print("No")

