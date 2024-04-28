import itertools
n = int(input())
nums = list(map(int, input().split()))
all_subsets = []
for r in range(0, len(nums)+1):
    all_subsets.extend(itertools.combinations(nums, r))
distinct_sums = set()
for subset in all_subsets:
    distinct_sums.add(sum(subset))
print(' '.join(map(str, sorted(distinct_sums))))
