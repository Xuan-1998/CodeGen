import sys

def max_joy_values():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in sys.stdin.readline().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == 1:
            dp[i][0] = a[0]
        else:
            for k in range(n):
                if k < 1:
                    dp[i][k] = a[i-1] + dp[i-1][k]
                elif k >= n:
                    dp[i][k] = c[i-1] + dp[i-1][k-1]
                else:
                    dp[i][k] = max(dp[i-1][k-1], dp[i-1][k]) + a[i-1]

    return dp[n][n-1]

print(max_joy_values())
