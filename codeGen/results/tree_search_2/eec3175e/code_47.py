def memoize(f):
    cache = {}
    def memoized_f(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return memoized_f

@memoize
def has_divisible_subset_sum(nums, m):
    dp = [False] * (m + 1)
    dp[0] = True

    for num in nums:
        for i in range(m, num - 1, -1):
            if not dp[i]:
                dp[i] = dp[i - num]
    return dp[m]

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(has_divisible_subset_sum(nums, m))
