===BEGIN CODE===
def distinct_sums(nums):
    n = len(nums)
    memo = {(i, s): [] for i in range(n+1) for s in range(sum(nums)+1)}
    
    def dp(i, s):
        if i > n or s < 0:
            return []
        if s > sum(nums):
            return []
        if (i, s) not in memo:
            if s == 0:
                res = [[]]
            else:
                res = [subset + [nums[i-1]] for subset in dp(i-1, s-nums[i-1])]
            memo[(i, s)] = res
        return memo[(i, s)]
    
    result = set()
    for i in range(1, n+1):
        for s in range(sum(nums)+1):
            result.update(dp(i, s))
    return sorted(list(result))

N = int(input())
nums = [int(x) for x in input().split()]
print(' '.join(map(str, distinct_sums(nums))))
===END CODE===
