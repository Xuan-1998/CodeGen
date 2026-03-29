import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

for task in range(k):
    l, r = map(int, input().split())
    column_sorted = True
    for i in range(l-1, r):
        if table[i][task] > table[i+1][task]:
            column_sorted = False
            break
    print("Yes" if column_sorted else "No")
