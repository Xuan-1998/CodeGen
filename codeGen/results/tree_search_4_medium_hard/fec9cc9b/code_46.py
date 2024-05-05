import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[1] * n for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[j] <= arr[i]:
            dp[i][j] = max(dp[i][j], dp[j][i-1] + 1)

for _ in range(m):
    l, r = map(int, input().split())
    non_decreasing_length = dp[r][r]
    for i in range(r-1, l-1, -1):
        if arr[i-1] >= arr[i]:
            non_decreasing_length -= 1
            while i > l and arr[i-2] <= arr[i-1]:
                i -= 1
        else:
            break
    print("Yes" if non_decreasing_length >= r-l+1 else "No")
