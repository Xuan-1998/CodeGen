import sys

def find_longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # If current element is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the longest increasing subsequence

    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)  # Count the occurrences of the maximum value in the DP array
    return count

# Receive input from stdin and print the answer to stdout
arr = list(map(int, input().split()))
print(find_longest_increasing_subsequences(arr))
