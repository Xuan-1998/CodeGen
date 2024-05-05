import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dynamic programming table

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(arr))
