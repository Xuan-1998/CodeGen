import sys

input_string = input().strip()
n = len(input_string)

# Initialize the DP table with False values
dp = [[False] * 2 for _ in range(n + 1)]

# Fill the table using bottom-up dynamic programming
for i in range(1, n + 1):
    if input_string[i - 1] == 'A':
        dp[i][0] = dp[i-1][1]
        dp[i][1] = dp[i-1][0] and input_string[i-2:i] == 'AB'
    elif input_string[i - 1] == 'B':
        dp[i][0] = dp[i-1][1] and input_string[i-2:i] == 'BA'
        dp[i][1] = dp[i-1][0]

# Check if there's a valid transition from either 'A' or 'B' to the end of the string
if dp[n][0] or dp[n][1]:
    print("YES")
else:
    print("NO")
