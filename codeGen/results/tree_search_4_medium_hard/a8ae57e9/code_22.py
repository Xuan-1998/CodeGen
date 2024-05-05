from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    s = [0] * (k + 1)

    for _ in range(n):
        c, p = map(int, input().split())
        if c > k:
            continue
        for i in range(c, 0, -1):
            dp[i] = max(dp[i], dp[i-1])
            s[i] += p
            if i <= k and s[i] > dp[i]:
                dp[i] = s[i]
        for i in range(k, c-1, -1):
            t[i-c+1] = min(t[i-c+1], i)
    total_money_earned = sum(s[i] for i in range(1, k+1) if dp[i])
    accepted_requests = len([i for i in range(n) if s[c] >= dp[c]])
    print(total_money_earned, accepted_requests)

t = defaultdict(int)
solve()
