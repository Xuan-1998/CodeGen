from itertools import combinations

def maxSum(nums, k):
    n = len(nums)
    res = 0
    for r in range(2, n+1):
        for sub in combinations(range(n), r):
            if all(sub[i] - sub[i-1] <= k for i in range(1, r)):
                res = max(res, sum(nums[i] for i in sub))
    return res

nums = [int(x) for x in input().split()]
k = int(input())
print(maxSum(nums, k))
