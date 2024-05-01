from collections import Counter

def count_ways(m, N, arr):
    dp = [0] * (N + 1)
    dp[0] = 1
    for num in arr:
        counter = Counter({n: dp[n] for n in range(N+1) if n >= num})
        for k, v in counter.items():
            dp[k] += v
    return dp[N]
