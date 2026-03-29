import sys

def read_input():
    return list(map(int, sys.stdin.readline().split()))

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

arr = read_input()
print(longest_increasing_subsequence(arr))
