from itertools import chain, combinations
n = int(input())
nums = [int(i) for i in input().split()]
all_sums = []
for r in range(1, n+1):
    for subset in chain(*map(lambda x: combinations(nums, x), range(r, 0, -1))):
        all_sums.append(sum(subset))
print(' '.join(map(str, sorted(set(all_sums)))))
