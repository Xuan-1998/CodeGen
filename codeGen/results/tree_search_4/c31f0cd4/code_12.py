from itertools import chain, combinations

def find_distinct_sums(nums):
    dp = {}
    for r in range(1, len(nums) + 1):
        for subset in combinations(nums, r):
            total = sum(subset)
            if total not in dp:
                dp[total] = [subset]
            else:
                dp[total].append(subset)

    distinct_sums = set()
    for k in sorted(dp.keys()):
        distinct_sums.add(k)

    return ' '.join(map(str, distinct_sums))

# Read input
N = int(input())
nums = list(map(int, input().split()))

print(find_distinct_sums(nums))
