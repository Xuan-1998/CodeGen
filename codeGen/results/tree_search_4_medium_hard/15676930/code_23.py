import sys

def max_hare_joys():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[-float('inf')] * (n+1) for _ in range(n+1)]

    for j in range(n+1):
        dp[0][j] = 0

    for i in range(1, n+1):
        for j in range(min(i+1, n)+1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j] + a[i-1], dp[i-1][j+1] + c[i-1])
            elif j == i:
                dp[i][j] = max(dp[i-1][j-1] + a[i-1], dp[i-1][j] + b[i-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + a[i-1], dp[i-1][j] + b[i-1], dp[i-1][j+1] + c[i-1])

    return max(dp[n])

print(max_hare_joys())
