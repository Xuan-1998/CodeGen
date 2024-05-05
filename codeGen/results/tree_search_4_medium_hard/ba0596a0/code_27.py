from sys import stdin

def can_cross_stones(stones):
    max_distance = stones[-1]
    dp = [[False] * (max_distance + 1) for _ in range(len(stones))]
    
    dp[0][0] = True
    for i, stone in enumerate(stones):
        if i > 0:
            for j in range(1, min(i, max_distance) + 1):
                if dp[i-1][j]:
                    if abs(stone - stones[i-1]) in [j-1, j, j+1]:
                        dp[i][j] = True
    
    return dp[-1][-1]

stones = list(map(int, stdin.readline().split()))
print(can_cross_stones(stones))
