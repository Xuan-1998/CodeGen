import sys
from collections import defaultdict

def find_LIS(arr):
    n = len(arr)
    dp = [1] * n
    max_length = 1
    count = defaultdict(int)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        count[dp[i]] += 1

    max_length = max(dp)
    return sum(count[max_length] >= 2, [])

# Read the array from stdin
n = int(input())
arr = list(map(int, input().split()))

print(len(find_LIS(arr)))
