import sys
from collections import defaultdict

def solve():
    n = int(input())
    t = input().strip()
    s = [input().strip() for _ in range(n)]

    dp = [[0] * (n + 1) for _ in range(len(t) + 1)]
    last_used = [-1] * (n + 1)

    for i in range(1, len(t) + 1):
        for j in range(1, n + 1):
            if t[i - 1] != s[j - 1][0]:
                dp[i][j] = dp[i - 1][j]
            else:
                last_used[j] = i
                if any(t[last_used[k]:i].find(s[m]) >= 0 for m in range(j + 1, n)):
                    dp[i][j] = min(dp[i - 1][k] for k in range(j)) + 1
                else:
                    dp[i][j] = dp[i - 1][j]

    if any(dp[-1][i] > 0 for i in range(n)):
        m = min(dp[-1])
        for j in range(1, n + 1):
            while dp[-1][j] > m:
                j -= 1
        print(m)
        for i in range(m - 1, -1, -1):
            if last_used[j] == i:
                print(f"{j} {i}")
                break
    else:
        print(-1)

if __name__ == "__main__":
    solve()
