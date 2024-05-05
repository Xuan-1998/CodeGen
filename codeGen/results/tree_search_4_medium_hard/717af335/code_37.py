def findXY(A, B):
    dp = [[0] * (B + 1) for _ in range(A + 1)]

    for i in range(A + 1):
        for j in range(B + 1):
            if i == 0 and j == 0:
                continue
            if i < j:
                dp[i][j] = -1
            elif i >= j and (i ^ j) == j:
                dp[i][j] = min(dp[A - i][B - j], i)
            else:
                dp[i][j] = min(dp[max(0, A - i)][max(0, B - (A - i))], i)

    return dp[A][B]

# Read input from stdin
A = int(input())
B = int(input())

# Print the result to stdout
print(findXY(A, B))
