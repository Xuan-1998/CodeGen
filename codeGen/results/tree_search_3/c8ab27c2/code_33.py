from collections import defaultdict

def shortest_uncommon_subsequence(S, T):
    # Calculate the length of the longest common suffix (LCS)
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if S[i] == T[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    # Find the shortest uncommon subsequence by subtracting LCS from S and T lengths
    if dp[0][0] == 0:
        return -1
    return min(m, n) - dp[m-1][n-1]

# Receive input from standard input
S = input()
T = input()

# Print the answer to standard output
print(shortest_uncommon_subsequence(S, T))
