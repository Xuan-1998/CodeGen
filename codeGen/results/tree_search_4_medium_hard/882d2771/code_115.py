import sys

def beauty_contest(l, r, t):
    MOD = 10**9 + 7

    dp = [0] * (r + 1)
    dp[1] = 0
    for i in range(2, r + 1):
        if l == i:
            dp[i] = 0
        else:
            if all(dp[k] - dp[k-1] >= 1 for k in range(l+1, i)):
                dp[i] = (i-1) * (i-2) // 2
            else:
                min_comparisons = float('inf')
                for k in range(i):
                    if all(dp[j] - dp[j-1] >= 1 for j in range(k+1, i)):
                        min_comparisons = min(min_comparisons, dp[k] + 2 * (i-k-1))
                dp[i] = min_comparisons

    return sum(t[i] * dp[i] for i in range(r-l+1)) % MOD

t, l, r = map(int, input().split())
print(beauty_contest(l, r, [int(x) for x in input().split()]))
