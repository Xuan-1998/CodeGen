# Step 1: Initialize variables
n = int(input())  # length of the message
s = input()  # the message itself
a = [int(x) for x in input().split()]  # the maximum number of times each character can appear consecutively

# Step 2: Create a 2D array to store the dynamic programming information
dp = [[0] * (n + 1) for _ in range(27)]

# Step 3: Fill up the dp array using dynamic programming
for i in range(n):
    for j in range(27):
        if i < a[j]:
            dp[j][i+1] = dp[j][i]
        else:
            if s[i-j+1].count(s[i-j]) <= a[j]:
                dp[j][i+1] = dp[j][i] + 1
            else:
                dp[j][i+1] = dp[j][i]

# Step 4: Calculate the number of ways to split the message into substrings
ways = dp[0][n]
for i in range(1, n):
    if s[i].count(s[i-1]) <= a[ord(s[i-1]) - ord('a')]:
        ways *= (dp[ord(s[i-1]) - ord('a')][i])
    else:
        break

# Step 5: Calculate the length of the longest substring and the minimum number of substrings
longest_substring = max((len(substring) for substring in s.split('.')), default=0)
min_substrings = len(s.split('.'))
