from collections import defaultdict

def solve():
    t = input().strip()
    n = int(input())
    s = [input().strip() for _ in range(n)]

    dp = [[float('inf')] * (n + 1) for _ in range(len(t) + 1)]
    dp[0] = [0] * (n + 1)

    for i, c in enumerate(t):
        if c in s:
            for j in range(1, n + 1):
                if c not in s[j-1]:
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j-1] + 1)

    m = dp[-1].index(min(dp[-1])) - 1
    steps = []
    for i in range(m, -1, -1):
        if dp[i+1][dp[i+1].index(min(dp[i+1]))] < dp[i][dp[i].index(min(dp[i]))]:
            j = dp[i+1].index(min(dp[i+1]))
            steps.append((j, i))
            dp[i][j] += 1
        else:
            break

    print(len(steps))
    for step in steps:
        print(*step)

solve()
