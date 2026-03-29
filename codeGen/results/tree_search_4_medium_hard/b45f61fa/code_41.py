def min_operations(p):
    n = len(p)
    dp = [[0]*n for _ in range(n)]
    result = ''

    # Initialize base case
    for k in range(n):
        dp[0][k] = p[0] * p[k+1]

    # Fill up the DP table
    for i in range(1, n):
        for j in range(i, n):
            if i == 1:
                dp[i][j] = dp[i-1][j] + p[i] * p[j+1]
            else:
                dp[i][j] = min([dp[i-1][k] + p[i]*p[k+1]*p[j] for k in range(i, j)])

    # Build the string of parentheses
    for i in range(1, n):
        for j in range(i+1, n):
            if dp[i][j] == dp[i-1][j]:
                result += str(p[i]) + ' '
            else:
                result = '(' + result

    # Add closing parentheses
    for _ in range(n - 2):
        result = '(' + result
    result = ')' * (n - 2) + result

    return result.strip()

# Test the function
p = [int(x) for x in input().split()]
print(min_operations(p))
