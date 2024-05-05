from collections import defaultdict

def max_grade(n, t):
    dp = [0] * (n + 1)
    memo = defaultdict(int)

    def update_memo(i, t):
        if memo[i] > 0:
            return memo[i]
        if i == 0:
            return 0
        time_taken = (i - n) // 10
        if time_taken <= t:
            dp[i] = max(dp[i-1], i)
        else:
            dp[i] = dp[i-1]
        memo[i] = dp[i]
        return dp[i]

    for i in range(1, n+1):
        t -= (i - n) // 10
        if t <= 0:
            break
        dp[i] = update_memo(i, t)

    return dp[-1]

n, t = map(int, input().split())
print(max_grade(n, t))
