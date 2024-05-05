from collections import defaultdict

def findXY(A, B):
    dp = defaultdict(int)
    dp[0][0][0] = 0
    
    for i in range(1, A+1):
        for j in range(1, B+1):
            for k in range(i):
                if (A-i == k + dp[k][j-1][0]) and (B-j == k ^ dp[k][j-1][0]):
                    dp[i][j][k] = min(dp[i][j][k], dp[k][j-1][0])
    
    for i in range(A+1):
        if dp[i][B][i] != 0:
            return "{} {}".format(i, B^i)
    
    return "-1"

A, B = map(int, input().split())
print(findXY(A, B))
