import sys

n = int(input())  # Read number of strings from input

costs = []  # List to store costs
strings = []  # List to store strings

for _ in range(n):
    cost, s = map(str.strip, input().split())  # Read cost and string from input
    costs.append(int(cost))  # Store cost as integer
    strings.append(s)  # Store string

max_len = max(len(s) for s in strings)  # Calculate maximum length of strings

dp = [[0] * (max_len + 1) for _ in range(n + 1)]  # Initialize 2D array for dynamic programming

for i in range(1, n + 1):
    for j in range(1, max_len + 1):
        dp[i][j] = min(dp[i-1][j], costs[i-1] + dp[i-1].min(j, len(strings[i-1]))))

ans = dp[n][max_len]

print(ans if ans < sys.maxsize else -1)  # Print answer
