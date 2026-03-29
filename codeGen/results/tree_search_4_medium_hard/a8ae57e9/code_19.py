from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    d = defaultdict(int)
    
    for i in range(1, n + 1):
        c, p = map(int, input().split())
        for j in range(min(c, k), -1, -1):
            dp[i][j] = max(dp[i-1][min(j, c)] + p, dp[i-1][j])
            d[(i, min(j, c))] = j
    
    return str(dp[-1][-1]) + '\n' + '\n'.join(f'{i+1} {d[(n, i)]+1}' for i in range(n))

print(solve())
