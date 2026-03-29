import sys

def is_ladder(arr, l, r):
    dp = [[True] * (r + 1) for _ in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(i, r + 1):
            if arr[j - 1] > arr[j]:
                dp[i][j] = False
            elif arr[j - 1] <= arr[j]:
                dp[i][j] = dp[i - 1][j]

    return all(dp[l][r])

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    print("Yes" if is_ladder(arr, l - 1, r) else "No")
