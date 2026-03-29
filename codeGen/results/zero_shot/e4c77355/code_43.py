import sys

def longest_increasing_subsequence():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * (n + 1)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(longest_increasing_subsequence())
