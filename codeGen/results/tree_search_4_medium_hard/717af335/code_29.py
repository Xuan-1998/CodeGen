import sys

def min_xor(A, B):
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 0
    
    for i in range(A + 1):
        for j in range(B + 1):
            if i >= j:
                dp[i][j] = min(dp[i - j][j - 1], i) + 1
            elif j > 0 and (B - j <= A or B - j < i):
                dp[i][j] = float('inf')
    
    X, Y = float('inf'), float('inf')
    for x in range(A + 1):
        for y in range(B + 1):
            if dp[x][y] != float('inf'):
                X, Y = x, y
                break
    
    return X, Y

A = int(input())
B = int(input())

X, Y = min_xor(A, B)

if X == float('inf'):
    print(-1)
else:
    print(X, Y)
