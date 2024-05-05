import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
state = [[0] * (n + 1) for _ in range(m)]

for i in range(1, m):
    for j in range(query[i][0], query[i][1] + 1):
        state[i][j] = max(state[i-1][k] for k in range(query[i][0], query[i][1] + 1) if (state[i-1][k-1] > 0 and a[k-1] >= a[k]) or (state[i-1][k-1] == 0 and a[k-1] >= a[k]))

for i in range(m):
    print("Yes" if state[m-1][query[i][1]] > state[m-1][query[i][0]] else "No")
