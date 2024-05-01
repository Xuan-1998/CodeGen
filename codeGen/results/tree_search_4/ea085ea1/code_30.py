### BEGIN CODE ###
from collections import defaultdict

def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the base case
    dp[0][0] = 0

    # Iterate over all possible substring lengths and start indices
    for k in range(1, N + 1):
        for i in range(N - k + 1):
            for j in range(N - k + 1):
                # Check if the current k-length substring is present in both str1 and str2
                if str1[i:i+k] == str2[j:j+k]:
                    dp[i][j] = max(dp[i][j], dp[i+k-1][j+k-1] + 1)
                else:
                    dp[i][j] = max(dp[i][j], max(dp[i+1][j], dp[i][j+1]))

    return max([dp[N-1][i] for i in range(N)])

### END CODE ###

# Read input from standard input
str1, str2 = [line.strip() for line in sys.stdin.readlines()]

# Call the function to find the maximum number of common non-overlapping substrings
max_count = max_common_substrings(str1, str2)

# Print the result to standard output
print(max_count)
