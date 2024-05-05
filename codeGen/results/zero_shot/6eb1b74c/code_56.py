import sys
from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    dp = [[-1 for _ in range(len(t) + 1)] for _ in range(n + 1)]
    dp[0] = list(range(len(t) + 1))

    for i in range(1, n + 1):
        for j in range(len(t) + 1):
            if dp[i - 1][j] == -1:
                dp[i][j] = -1
            else:
                k = j
                while k > 0 and t[k - 1] != s[i - 1][-1]:
                    k -= 1
                if k > 0:
                    dp[i][j] = min(dp[i - 1][k - 1], j) + (1 if i > 1 else 0)

    m = 0
    while m < len(t):
        for i in range(1, n + 1):
            k = len(t) - 1
            while k >= 0 and t[k] != s[i - 1][-1]:
                k -= 1
            if k >= 0:
                print(i, k + 1)
                m = max(m, k)
                break

    print(-1) if m < len(t) else None

if __name__ == "__main__":
    solve()
