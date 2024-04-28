# Read input from stdin
n, k = map(int, input().split())

# Create a 2D array to store the state information
dp = [[0] * (k + 1) for _ in range(n + 1)]

# Base case: There's only one good sequence of length 1 ending with i and having i as its last multiple divisor
for i in range(1, n + 1):
    dp[i][1] = 1

# Calculate the number of good sequences of length k ending with i and having j as its last multiple divisor
for len_ in range(2, k + 1):
    for i in range(len_, n // (len_ - 1) + 1):  # Loop from i to n / (k - 1)
        for j in range(i, min(n // (i - 1), i) + 1):  # Loop from j to min(n / (i - 1), i)
            dp[i][len_] += dp[j][len_ - 1]

# Calculate the count of good sequences modulo 10000
mod = 10**9 + 7
count = sum(dp[i][k] for i in range(1, n + 1))
print(count % mod)

