import sys

# Initialize the DP table with a size of 501x501 to accommodate for the base case dp[0][0] = 0
dp = [[-1 for _ in range(501)] for _ in range(501)]

def uncommon_subsequence(S, T):
    m, n = len(S), len(T)
    
    # Base case: dp[0][0] = 0
    dp[0][0] = 0

    # Iterate over the characters in both strings
    for i in range(m + 1):
        for j in range(n + 1):
            if S[i-1] == T[j-1]:  # If the current characters match, increment the length by 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:  # If the characters don't match, update the DP table with the maximum of the previous lengths
                if i > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:  # Base case for S being empty
                    dp[i][j] = j

    # Return the minimum length of a subsequence that ends with the last character in either string - 1
    return min(max((m, n)[0]), max((m, n)[1])) if all(x == -1 for row in dp for x in row) else -1

# Input strings S and T from standard input
S = input()
T = input()

# Output the result to standard output
print(uncommon_subsequence(S, T))
