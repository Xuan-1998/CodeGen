code
from collections import defaultdict

# Read input strings
N = int(input())
str1 = input()
str2 = input()

# Create a hashmap to store characters in str2
char_map = defaultdict(int)
for char in str2:
    char_map[char] += 1

# Initialize DP table
dp = [[0] * (N + 1) for _ in range(N + 1)]

# Fill DP table
max_count = 0
for i in range(N):
    for j in range(N):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_count = max(max_count, dp[i][j])

print(max_count)
