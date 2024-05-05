import sys
from collections import defaultdict

def longest_increasing_subsequences(arr):
    dp = [1] * len(arr)
    count_map = defaultdict(int)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        count_map[dp[i]] += 1

    max_length = max(dp)
    return sum(1 for k in count_map if k == max_length)

# Read input
arr = list(map(int, sys.stdin.readline().strip().split()))
print(longest_increasing_subsequences(arr))
