n = int(input())
a = list(map(int, input().split()))

# Initialize the dp array with the base case values
dp = [n - i for i in range(n)]

# Iterate over the array from right to left
for i in range(n - 1, -1, -1):
    # Look for a j such that a[i] can be merged with a[j]
    j = i + 1
    while j < n:
        if a[i] == a[j]:
            # Merge a[i] and a[j] and update dp[i]
            dp[i] = min(dp[i], (j - i - 1) + dp[j + 1] if j + 1 < n else 1)
            break
        elif a[i] < a[j]:
            # If a[j] is greater, we cannot merge a[i] with a[j]
            break
        j += 1

# The answer is the minimum possible length of the array starting from the first element
print(dp[0])
