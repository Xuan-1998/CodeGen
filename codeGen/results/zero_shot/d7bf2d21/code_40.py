import sys

# Read input from stdin
n = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().strip().split()))

# Initialize dp array to store lengths of LISs
dp = [1] * n

# Compute lengths of all LISs using dynamic programming
for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Count the number of LISs with maximum length
max_length = max(dp)
count = sum(1 for x in dp if x == max_length)

print(count)
