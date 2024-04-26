n = int(input())
a = list(map(int, input().split()))

# Initialize the DP table
dp = [1] * n

# Iterate from the end of the array to the beginning
for i in range(n - 2, -1, -1):
    # If the current and next elements are the same, try to merge them
    if a[i] == a[i + 1]:
        # Look for the position after the next element where the merge is possible
        j = i + 2
        while j < n and a[j] == a[i] + 1:
            a[i] += 1  # Increment the value after merging
            j += 1
        # Update the DP table considering the merging
        dp[i] = min(dp[i], (dp[j] if j < n else 0) + 1)
    else:
        # If no merging is possible, the length is the same as the next element's DP value plus one
        dp[i] = dp[i + 1] + 1

# The answer is the minimum length of the entire array
print(dp[0])
