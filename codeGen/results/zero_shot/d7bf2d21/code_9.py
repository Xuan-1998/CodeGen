import sys
from collections import defaultdict

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    parent = defaultdict(list)

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[dp[i]].append(arr[i])

    max_length = max(dp)
    longest_subsequences = [subsequence for subsequence in parent[max_length]]

    return len(longest_subsequences)

arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
