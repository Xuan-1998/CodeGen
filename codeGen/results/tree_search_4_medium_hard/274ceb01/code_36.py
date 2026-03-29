n = int(input())
marks_above_water = list(map(int, input().split()))

dp = [[0] * (i+1) for i in range(n+1)]

for i in range(1, n+1):
    for k in range(min(i, marks_above_water[i-1]), -1, -1):
        if k == 0:
            dp[i][k] = min(dp[j][m] + (i-j)*m for j in range(i) for m in range(k+1))
        else:
            dp[i][k] = min(dp[j][m] + (i-j)*m for j in range(i) for m in range(min(k, marks_above_water[j-1])))
        
print(min(dp[n]))
