import sys

def road_gas(n, w, roads):
    dp = [[0] * (sum(w) + 1) for _ in range(n)]
    
    dp[0][w[0]] = w[0]
    
    for i in range(1, n):
        for j in range(sum(w), -1, -1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][k] for k in range(j, min(j+w[i], sum(w) + 1)))
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[-1][-1]

n = int(input())
w = [int(x) for x in input().split()]
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u-1, v-1, c))
print(road_gas(n, w, roads))
