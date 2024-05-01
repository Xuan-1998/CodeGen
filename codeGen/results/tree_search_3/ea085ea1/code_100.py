N = int(input())
str1, str2 = input().split()

# Initialize 2D table with zeros
dp = [[0] * (N + 1) for _ in range(N + 1)]

max_common_substrings = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if str1[i - 1] == str2[j - 1]:
            # If the characters match, increment the count
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_common_substrings = max(max_common_substrings, dp[i][j])
        else:
            # If the characters don't match, reset the count
            dp[i][j] = 0

print(max_common_substrings)
