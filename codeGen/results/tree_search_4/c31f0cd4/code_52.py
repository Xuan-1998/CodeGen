===BEGIN CODE===
from collections import defaultdict

def distinct_sums(nums):
    N, *nums = map(int, input().split())
    dp_state = [[set() for _ in range(N+1)] for _ in range(N+1)]
    memo = defaultdict(set)

    def dfs(i, s):
        if i == 0:
            return {s}
        if (i, s) not in memo:
            sums = set()
            for ai in [nums[i-1]] + [0]:
                new_sums = dfs(i-1, s+ai)
                if ai > 0:
                    new_sums = {s_sum + ai for s_sum in new_sums}
                sums.update(new_sums)
            memo[(i, s)] = sums
        return memo[(i, s)]

    distinct_sums_set = set()
    for i in range(N+1):
        for s in range(sum(nums)+1):
            if (0 <= s <= sum(nums) // 2 or s == sum(nums) // 2):
                distinct_sums_set.update(dfs(i, s))

    return ' '.join(map(str, sorted(distinct_sums_set)))

print(distinct_sums(input().split()))
