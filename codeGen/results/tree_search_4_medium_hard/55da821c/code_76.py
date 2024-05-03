import sys

def min_replantments():
    n, m = map(int, input().split())
    dp = [[sys.maxsize] * m for _ in range(n)]
    last_s = None
    for i in range(n):
        s, x = map(int, input().split())
        if i > 0:
            for j in range(m):
                if abs(x - (i-1) * (m+1)) < abs((j+1) * (m+1) - i*m - m):
                    last_s = j
                    break
        dp[i][s-1] = min(dp[i][s-1], dp[max(0, i-1)][last_s-1] + 1)
    print(min(dp[-1]))

min_replantments()
