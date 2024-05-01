import sys

def find_max_common_substrings():
    N = int(sys.stdin.readline().strip())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    # Initialize a 2D array to store the lengths of common substrings
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Initialize the maximum count of common non-overlapping substrings
    max_common_substr_count = 0

    # Iterate over the strings using a sliding window approach
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Check if the current characters match and update the dp array accordingly
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the maximum count of common non-overlapping substrings
                max_common_substr_count = max(max_common_substr_count, dp[i][j])

    return max_common_substr_count

print(find_max_common_substrings())
