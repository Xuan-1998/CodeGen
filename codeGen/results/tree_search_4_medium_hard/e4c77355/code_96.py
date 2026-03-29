import sys
from collections import defaultdict

def longest_increasing_subsequence():
    n = int(input())
    seq = list(map(int, input().split()))
    dp = [1] * n
    prev = [None] * n

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    max_length = max(dp)
    indices = [i for i, x in enumerate(dp) if x == max_length]
    return max_length

print(longest_increasing_subsequence())
