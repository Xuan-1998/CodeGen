import sys

def min_replants(n, m):
    plants = sorted([(s, x) for s, x in zip(*[map(int, line.split()) for line in [line.strip().split() for line in sys.stdin][1:]])), key=lambda x: x[1])
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if plants[i - 1][0] == j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) if i > 0 else 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j]) if i > 0 else 0
                
    return dp[-1][-1]

n, m = map(int, input().split())
print(min_replants(n, m))
