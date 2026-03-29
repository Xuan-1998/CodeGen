import sys

def f(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i // 2, -1, -1):
            if i % j == 0 and dp[j] > 0:
                dp[i] += dp[j]
                break
    return dp[n]

t, l, r = map(int, input().split())
ans = t * f(l) + sum(ti * f(li) for ti, li in zip(map(int, input().split()), range(l + 1, r + 1))) - l * f(r)
print(ans % (10**9 + 7))
