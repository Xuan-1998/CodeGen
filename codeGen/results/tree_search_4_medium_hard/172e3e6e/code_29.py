import sys
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    memo = defaultdict(int)

    for i in range(1, n + 1):
        if a[i - 1] == 0:
            continue

        for j in range(i):
            if a[j] % (j + 1) != 0 or memo[(a[j], j)] != dp[j]:
                break
        else:
            dp[i] = (dp[i - 1] + dp[j]) % (10**9 + 7)
            for k in range(j, i):
                memo[(a[k], k)] = dp[k]

    print(dp[-1])

if __name__ == "__main__":
    solve()
