import sys

def solve(n, k):
    memo = {}
    dp = [""] * (k + 1)

    def transition(s, deleted):
        if len(s) == 0 or (deleted and len(s) > 1):
            return min(s, s + s), True
        elif len(s) < k:
            return max(s, s + s), False
        else:
            return s, deleted

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = min(dp[i - 1], transition(dp[i - 1], True)[0])
        else:
            dp[i] = dp[k]

    return dp[k].ljust(k)

n, k = map(int, sys.stdin.readline().split())
print(solve(n, k))
