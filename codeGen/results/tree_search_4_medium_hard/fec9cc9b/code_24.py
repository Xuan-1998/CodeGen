import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[False] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m):
        l, r = map(int, input().split())
        if all(arr[k-1] <= arr[k] for k in range(l, r+1)):
            dp[i][j] = True
        else:
            for k in range(l, r+1):
                prev = min((sys.maxsize, k - 1) + (0,)) if k > l else None
                next = max((sys.maxsize, k + 1) - (r,)) if k < r else None
                if arr[k-1] <= arr[k] and arr[k] >= arr[k+1]:
                    dp[i][j] = True
                    break

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if dp[n][r-l+1] else "No")
