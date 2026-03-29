# Initialize variables
n = int(input())  # Read the number of hares
a = list(map(int, input().split()))  # Read the joy values for both adjacent hares being hungry
b = list(map(int, input().split()))  # Read the joy values for one full adjacent hare
c = list(map(int, input().split()))  # Read the joy values for both adjacent hares being full

# Create a dp array to store the maximum total joy for each hare's position
dp = [0] * n

# Calculate the maximum total joy for each hare's position
for i in range(n):
    if i == 0:
        # For the first hare, consider only the case where both adjacent hares are full
        dp[i] = c[0]
    elif i == n - 1:
        # For the last hare, consider only the case where its previous adjacent hare is full
        dp[i] = max(c[n-1], b[n-2] + dp[i-1])
    else:
        # For other hares, consider all three cases and take the maximum
        dp[i] = max(a[i] + (dp[i-1] if i > 0 else 0) + (dp[i+1] if i < n-1 else 0),
                    b[i] + dp[i-1],
                    c[i] + (dp[i-1] if i > 0 else 0) + (dp[i+1] if i < n-1 else 0))

# The maximum total joy is stored in the last position of the dp array
print(dp[-1])
