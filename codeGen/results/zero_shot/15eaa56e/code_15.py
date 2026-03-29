import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for l, r in [map(int, line.split()) for line in sys.stdin.read().strip().split('\n')[1:]]:
    column_sorted = any(all(table[i][j] <= table[i+1][j] for i in range(l-1, r)) for j in range(m))
    print("Yes" if column_sorted else "No")
