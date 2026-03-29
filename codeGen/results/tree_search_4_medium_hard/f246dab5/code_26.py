import sys

def solve(n):
    t_min = 0  # minimum time of all trips
    dp = [0] * (n + 1)  # dynamic programming array

    for i in range(1, n+1):
        if i - t_min >= 140:  # new 1-day ticket starts
            dp[i] = min((dp[j-1] + 120) for j in range(i-139,-1,-1))
        elif i - t_min >= 90 and i - t_min < 140:  # new 90-minute ticket starts
            dp[i] = min((dp[j-1] + 50) for j in range(i-89, -1, -1))
        else:  # new single-trip ticket starts
            dp[i] = dp[i-1] + 20

    return [str(int(dp[i])) for i in range(1, n+1)]

n = int(sys.stdin.readline())
print(*solve(n), sep='\n')
