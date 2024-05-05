import sys

def min_mana(n, k, h):
    dp = [0] + [sys.maxsize] * (max(k) + 1)
    for i in range(1, n+1):
        j = k[i-1]
        while j > 0:
            dp[j] = min(dp[j], max(0, dp[j-1]) + h[i-1])
            j -= 1
    return sum(dp)

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(min_mana(n, k, h))
