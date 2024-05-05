from sys import stdin

def frog_crosses(stones):
    n = len(stones)
    dp = [[False] * (stones[-1] + 1) for _ in range(n)]
    
    dp[0][stones[0]] = True
    
    for i in range(1, n):
        if i == 1:
            for j in range(max(0, stones[i-1] - k), min(stones[-1], stones[i-1] + k) + 1):
                if dp[i-1][j]:
                    dp[i][j] = True
        else:
            for j in range(max(0, stones[i-2] - k), min(stones[-1], stones[i-1] + k) + 1):
                if dp[i-2][j]:
                    dp[i][max(j-k+1, 0):min(j+k+1, len(stones)-1)].count(True) > 0
                    dp[i][j] = True
    
    return dp[-1][-1]

k = int(stdin.readline())
stones = list(map(int, stdin.readline().split()))
print(frog_crosses(stones))
