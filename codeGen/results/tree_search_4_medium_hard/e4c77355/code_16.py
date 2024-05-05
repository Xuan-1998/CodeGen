# Initialize dp array with 1s, since the longest increasing subsequence for a single element is always 1.
dp = [1] * len(arr)

max_length = 0

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            # Update dp[i] to be the maximum length of any increasing subsequence that ends with this element
            dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(max_length, dp[i])

print(max_length)
