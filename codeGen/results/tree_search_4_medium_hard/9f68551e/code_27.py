import sys

def solve():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    dp = [0] + [sys.maxsize] * (max(k) - 1)
    for i in range(len(k)):
        while dp[k[i]] > h[i]:
            dp[k[i]] = min(dp[k[i]], dp[k[i]-1] + 1)

    print(min(dp))

solve()
