from collections import defaultdict

def find_winners(M, X):
    # Initialize dp array with default value -1
    dp = [-1] * (X + 1)

    # Base case: only one person remains
    dp[0] = 1

    for i in range(1, X + 1):
        if i % M == 0:
            dp[i] = 1 + (dp[i - M] or 0)
        else:
            dp[i] = 1 + (dp[(i - 1) % M] or 0)

    return [x for x in dp[1:]]

# Example usage
M, X = map(int, input().split())
print(*find_winners(M, X), sep='\n')
