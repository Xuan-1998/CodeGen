import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with all ones (single elements are increasing subsequences)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] if we find a longer increasing subsequence

    return max(dp)  # Return the maximum length of all increasing subsequences

if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(arr))
