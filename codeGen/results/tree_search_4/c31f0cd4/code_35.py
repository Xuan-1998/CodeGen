from collections import defaultdict

def distinct_subset_sums(N, nums):
    seen = set()
    dp = defaultdict(int)

    for i in range(1, N + 1):
        for j in range(i + 1):
            subset_sum = sum(nums[:j])
            if subset_sum not in seen:
                seen.add(subset_sum)
            dp[subset_sum] += 1

    return ' '.join(map(str, sorted(seen)))

N = int(input())
nums = list(map(int, input().split()))
print(distinct_subset_sums(N, nums))
