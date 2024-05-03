import sys

def make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[False, float('inf')] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        if arr[i - 1] == 0:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0] or dp[i - 1][0]

        if arr[i - 1] > 0:
            dp[i][1] = min(dp[i][1], dp[i - 1][1])
        else:
            dp[i][1] = dp[i - 1][1]

    print("YES" if dp[n][0] else "NO")

make_zero()
