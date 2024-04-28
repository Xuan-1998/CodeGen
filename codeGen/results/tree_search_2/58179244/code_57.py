from collections import defaultdict

def min_recolor(n, colors):
    memo = {}
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        if i == 1:
            prev_color = None
        else:
            prev_color = colors[i - 2]
        state = (i, prev_color)
        if state not in memo:
            count = 0
            for j in range(i):
                if colors[j] == prev_color:
                    count += 1
            dp[i] = min(dp[i], count + dp[j])
            memo[state] = dp[i]
    return dp[n]

n = int(input())
colors = input().strip()
print(min_recolor(n, colors))
