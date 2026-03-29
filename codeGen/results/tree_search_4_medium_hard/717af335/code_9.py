# Read input from standard input
A, B = map(int, input().split())
dp = [[float('inf')] * (B+1) for _ in range(A+1)]
dp[0][0] = 0

for i in range(A+1):
    for j in range(B+1):
        if i < j:
            continue
        if i >= j:
            for k in range((i+j)//2 + 1):
                x = 2*k
                y = i - 2*k
                if (x ^ y) == j and dp[i-x][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], x)
                x = 2*k + 1
                y = i - 2*k - 1
                if (x ^ y) == j and dp[i-x-1][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], x)

# Print the result to standard output
if dp[A][B] == float('inf'):
    print(-1)
else:
    print(dp[A][B])
