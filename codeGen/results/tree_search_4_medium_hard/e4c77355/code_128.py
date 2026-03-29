n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n  # Initialize dp with all ones (subsequences of length 1)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:  # Check if current element is greater than previous
            dp[i] = max(dp[i], dp[j] + 1)  # Update maximum length

print(max(dp))  # Print the maximum length (longest increasing subsequence)
