from collections import defaultdict

dp = defaultdict(int)

def minRemovals(signs, queries):
    n, q = len(signs), 0
    for _ in range(q):
        l, r = map(int, input().split())
        prefix_sum = sum(1 if signs[i] == '+' else -1 for i in range(l-1))
        suffix_sum = sum(1 if signs[i] == '+' else -1 for i in range(r, n-1, -1))
        dp[r] += min(prefix_sum, suffix_sum)
        for i in range(l-1, r):
            dp[i] += 1 if signs[i] != (prefix_sum < 0) ^ (suffix_sum < 0) else 0
    return max(dp.values(), default=0)

n = int(input())
signs = list(input())

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(minRemovals(signs, [l, r]))
