===BEGIN CODE===
from collections import defaultdict
def solve():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        signs = list(input())
        prefix_sum = [0] + [1 if sign == '+' else -1 for sign in signs]
        dp = defaultdict(int)
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = min(dp[i-1], abs(sum(prefix_sum[:i])))
        ans = 0
        for _ in range(q):
            l, r = map(int, input().split())
            if prefix_sum[r] - prefix_sum[l-1] == 0:
                ans += 0
            else:
                ans += min(dp[r], dp[l-1] + abs(sum(prefix_sum[l:r])))
        print(ans)

solve()
