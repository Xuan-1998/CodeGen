import sys

def solve(table, n, m):
    for j in range(m):
        sorted_column = True
        prev_value = table[0][j]
        for i in range(1, n):
            if table[i][j] < prev_value:
                sorted_column = False
                break
            prev_value = table[i][j]
        if sorted_column:
            return "Yes"
    return "No"

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(sys.stdin.readline())
tasks = []
for _ in range(k):
    l, r = map(int, sys.stdin.readline().split())
    tasks.append((l-1, r-1))

print(solve(table, n, m))
