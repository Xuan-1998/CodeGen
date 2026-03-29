import sys

def is_non_decreasing_column(table, l, r):
    max_val = table[l-1][0]
    count = 1

    for i in range(l, r+1):
        if table[i-1][0] <= table[i][0]:
            count += 1
        else:
            return False
        max_val = max(max_val, table[i][0])

    return True

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(sys.stdin.readline())

for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    if is_non_decreasing_column(table, l, r):
        print("Yes")
    else:
        print("No")
