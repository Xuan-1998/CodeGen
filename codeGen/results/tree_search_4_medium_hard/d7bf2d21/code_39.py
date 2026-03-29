import sys

def longest_increasing_subsequences_count(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with 1s
    max_length = 1  # Maximum length seen so far
    count = 0  # Count of maximum length subsequences

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
        count += dp.count(max_length)

    return count

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

print(longest_increasing_subsequences_count(arr))
