import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
state = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    state[i][0] = 1 if a[i - 1] == max(a[:i]) else 0

for j in range(1, m + 1):
    for i in range(j - 1, -1, -1):
        for k in range(i, n + 1):
            state[k][j] = max(state[k][j], state[k - 1][j - 1] + 1 if a[k - 1] >= a[k] else 0)

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if state[r][l] > 0 else "No")
