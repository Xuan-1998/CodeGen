import sys

# Read the input string from stdin
s = input().strip()

# Initialize the boolean variables
abAppears, baAppears = False, False

# Create a 2D array to store dynamic programming values
dp = [[False] * 2 for _ in range(len(s) + 1)]

# Fill the dp table
for i in range(1, len(s) + 1):
    if s[i - 1:i+1] == 'AB':
        dp[i][0] = True
    elif s[i - 1:i+1] == 'BA':
        dp[i][1] = True
    for j in range(max(i // 2, 1), 0, -1):
        if i >= j and (dp[i - j][0] or dp[i - j][1]):
            if s[i - j:i] == 'A' and not abAppears:
                abAppears = True
            elif s[i - j:i] == 'B' and not baAppears:
                baAppears = True

# Print the result to stdout
print("YES" if (abAppears or baAppears) else "NO")
