import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP table with ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum length of LIS

if __name__ == "__main__":
    arr = list(map(int, input().split()))  # Read input array
    print(longest_increasing_subsequence(arr))  # Print the result
