code
from collections import defaultdict

def uncommonFromS(S, T):
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    
    # Initialize the DP table with base cases
    for i in range(1, len(S) + 1):
        dp[i][0] = i
    
    for j in range(1, len(T) + 1):
        dp[0][j] = j
    
    char_indices = defaultdict(list)
    
    # Store the indices of characters in string T as keys and their corresponding values
    for i, c in enumerate(S):
        if c not in char_indices:
            char_indices[c] = [i]
        else:
            char_indices[c].append(i)
    
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] != T[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i - 1][j - 1]
    
    # Find the minimum value of dp[i][j] for all i and j as the result
    return min(min(row) for row in dp) if any(dp[i][j] < len(S) + len(T) for i, row in enumerate(dp) for j in row) else -1

S = input().strip()
T = input().strip()

print(uncommonFromS(S, T))
