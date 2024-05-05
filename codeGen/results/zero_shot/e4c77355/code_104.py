import sys

def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)

    for i, x in enumerate(arr):
        for j in range(i):
            if x > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
