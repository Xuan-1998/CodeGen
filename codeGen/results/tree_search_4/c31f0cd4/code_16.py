from functools import lru_cache

@lru_cache(None)
def subsets_sum(subset):
    return set([sum(subset), *map(lambda x: sum(x), map(list, itertools.chain.from_iterable(itertools.combinations(subset, r) for r in range(1, len(subset)+1))))])

N = int(input())
nums = list(map(int, input().split()))
distinct_sums = set()
for r in range(1 << N):
    subset = [x for x in nums if (r & (1 << (nums.index(x))))]
    distinct_sums.update(subsets_sum(subset))

print(*sorted(distinct_sums), sep=' ')
