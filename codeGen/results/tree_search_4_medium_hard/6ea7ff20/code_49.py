import sys

def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (len(p)) for _ in range(len(p))]

    for i in range(n):
        for j in range(i+1, len(p)):
            if p[i] == p[j]:
                dp[i][j] = False
            elif not any(k in p[:i] or k in p[i:j] for k in set(p[:i])):
                dp[i][j] = True

    return "YES" if all(dp[i][len(p)-1] for i in range(n)) else "NO"

n_cases = int(input())
for _ in range(n_cases):
    n = int(input())
    p = list(map(int, input().split()))
    print(mergeable(p))
