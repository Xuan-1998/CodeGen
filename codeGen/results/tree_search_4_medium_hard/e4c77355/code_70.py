import sys
from collections import defaultdict

def longest_increasing_subsequence():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = defaultdict(lambda: 1)
    prev = [-sys.maxsize]
    for x in arr:
        idx = binary_search(prev, x)
        dp[x] = max(dp[x], dp[prev[idx]] + 1)
    
    return max(dp.values())

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(longest_increasing_subsequence())
