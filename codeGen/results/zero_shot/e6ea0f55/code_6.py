from itertools import combinations
import sys

n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = 0

for r in range(1, n+1):
    for subseq in combinations(range(n), r):
        if max(subseq) - min(subseq) <= k:
            curr_sum = sum(nums[i] for i in subseq)
            if curr_sum > max_sum:
                max_sum = curr_sum

print(max_sum)
