import sys

def is_ladder(arr, l, r):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[i - 1] <= arr[j]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[l][r]

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
