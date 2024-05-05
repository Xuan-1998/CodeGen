import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with base case values (dp[i] = 1 for all i)

    memo = {}  # Memoization dictionary to cache intermediate results

    for i in range(n):
        for j in range(i):  # Consider all previous elements y such that y < x
            if arr[j] <= arr[i]:  # Check if y is less than or equal to x
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] with the maximum length found

        memo[i] = dp[i]  # Cache intermediate result in memo dictionary

    return max(memo.values())  # Return the length of the longest increasing subsequence

# Read input from stdin
arr = list(map(int, input().split()))

print(longest_increasing_subsequence(arr))
