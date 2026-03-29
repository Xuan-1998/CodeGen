def solve():
    n = int(input())
    portals = list(map(int, input().split()))
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    
    for i in range(2, n+1):
        if (portals[i-1]%2==1 and dp[i-1][portals[i-1]]!=0) or (portals[i-1]%2==0 and dp[i-1][portals[i-1]-1]!=0):
            for j in range(1, i+1):
                if (j==i and dp[j][i]!=0) or (j<i and dp[j][i-1]!=0):
                    dp[i][i] += 1
        else:
            for j in range(1, i+1):
                if (j==i and dp[j][i]!=0) or (j<i and dp[j][i-1]!=0):
                    dp[i][i-1] += 1
    
    return (dp[n][n]) % 1000000007

print(solve())
