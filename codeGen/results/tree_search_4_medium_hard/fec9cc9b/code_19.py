import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] >= arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

mem = [[False] * (n+1) for _ in range(m)]

for i in range(m):
    l, r = map(int, input().split())
    is_ladder = True
    for j in range(l-1, r):
        if arr[j] > arr[j+1]:
            is_ladder = False
            break
    print("Yes" if mem[i][r] or (not is_ladder) else "No")
