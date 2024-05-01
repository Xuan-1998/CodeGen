from collections import defaultdict

def common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N) for _ in range(N)]

    # Initialize memo with zeros
    memo = defaultdict(int)

    # Base case: When i or j is 0, there are no substrings.
    for i in range(N):
        dp[i][0] = dp[0][i] = 0

    # Transition rule:
    for i in range(1, N):
        for j in range(1, N):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

# Read input from standard input
str1 = input().strip()
str2 = input().strip()

print(common_substrings(str1, str2))
