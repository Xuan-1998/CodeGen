import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n
    max_length = 1
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return sum(1 for x in dp if x == max_length)

arr = list(map(int, input().split()))
print(longest_increasing_subsequences(arr))
