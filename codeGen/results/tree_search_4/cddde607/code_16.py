===BEGIN CODE===
from collections import namedtuple

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

Path = namedtuple('Path', 'i j')

def solve(k, n, arr):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1][j - 1] <= k:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i == j:
                if arr[i - 1][j - 1] == k:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
    
    return dp[0][0]

print(solve(K, N, arr))
