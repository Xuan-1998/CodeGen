import sys

def longest_increasing_subsequence():
    n = int(input())
    dp = [1] * n  # Initialize dp array with all ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

arr = list(map(int, input().split()))
print(longest_increasing_subsequence())
