# Read input from stdin
m = int(input())
n = int(input())
arr = list(map(int, input().split()))

# Initialize a dictionary to store memoized values
dp = {0: 1}

# Calculate the number of ways to reach each sum
for i in range(m):
    for j in range(n + 1):
        if arr[i] <= j:
            dp[j] = (dp.get(j, 0) + dp.get(j - arr[i], 0)) % (10**9 + 7)

# Print the result to stdout
print(dp[n])
