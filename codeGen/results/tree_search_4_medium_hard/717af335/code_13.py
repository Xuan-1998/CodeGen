def findX(A, B):
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 0
    
    for i in range(1, A + 1):
        for j in range(1, B + 1):
            if i < j:
                dp[i][j] = min(dp[i-1][j-1] + 2 * (i - 1) + j - i, dp[j-i][j])
            elif i > j:
                dp[i][j] = min(dp[i-1][j] + 2 * (i - 1) + j - i, dp[i][j-j])
    
    if dp[A][B] == float('inf'):
        return -1
    else:
        return X

A = int(input())
B = int(input())

X = findX(A, B)
print(X, end=' ')
print(B ^ X)

