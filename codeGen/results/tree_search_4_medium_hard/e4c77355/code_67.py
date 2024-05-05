import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Test the function
arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
