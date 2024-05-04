import sys

def min_bookcase_height(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        thickness, height = map(int, input().split())
        for w in range(m, thickness - 1, -1):
            if height > dp[i-1][w]:
                dp[i][w] = min(dp[i-1][w], height + dp[i-1][w-thickness])
    
    return max(max(row) for row in dp)

n, m = map(int, input().split())
print(min_bookcase_height(n, m))
