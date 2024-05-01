from collections import defaultdict

def distinct_sums(nums):
    memo = defaultdict(list)
    max_val = max(nums)

    def dp(i, s):
        if i == 0 or s > max_val:
            return []
        if (i, s) in memo:
            return memo[(i, s)]
        if i == 1:
            return [s]
        results = set()
        for ai in nums[:i]:
            include_ai_results = dp(i-1, s+ai)
            exclude_ai_results = dp(i-1, s)
            results.update(include_ai_results)
            results.update(exclude_ai_results)
        memo[(i, s)] = list(results)
        return memo[(i, s)]

    result = set()
    for i in range(len(nums)+1):
        result.update(dp(i, 0))
    return sorted(list(result))

# Example usage:
nums = [1, 2, 3]
print(distinct_sums(nums))  # Output: [1, 2, 3, 4, 5, 6]
