def f(i):
    if i <= 1:  # base case
        return 0
    if i in dp:
        return dp[i]
    min_comparisons = float('inf')
    for prev in range(1, i):
        comparisons = f(prev + 1) + (i - prev - 1)
        min_comparisons = min(min_comparisons, comparisons)
    dp[i] = min_comparisons + 1
    return dp[i]

t, l, r = map(int, input().split())
dp = {1: 0}  # initialize cache

print((t * (f(r) - f(l))) % (10**9 + 7))
