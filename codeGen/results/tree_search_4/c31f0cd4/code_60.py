from itertools import chain, combinations

def powerset(s):
    return chain(*map(lambda x: combinations(s, x), range(0, len(s) + 1)))

def find_distinct_sums(nums):
    dp_subsets = {(tuple(),): 0}
    dp_sums = {0}

    for num in nums:
        new_subsets = set()
        for subset, subset_sum in list(dp_subsets.items()):
            new_subset = tuple(list(subset) + [num])
            new_subset_sum = subset_sum + num
            if new_subset not in dp_subsets:
                dp_subsets[new_subset] = new_subset_sum
                new_sums = {new_subset_sum}
                for other_subset, other_subset_sum in list(dp_subsets.items()):
                    new_sum = other_subset_sum + num
                    if new_sum not in dp_sums and new_subset != other_subset:
                        dp_sums.add(new_sum)
            new_sums = set()
            for subset, subset_sum in list(dp_subsets.items()):
                new_subset = tuple(list(subset) + [num])
                new_subset_sum = subset_sum + num
                if new_subset not in dp_subsets:
                    dp_subsets[new_subset] = new_subset_sum
                    for other_subset, other_subset_sum in list(dp_subsets.items()):
                        new_sum = other_subset_sum + num
                        if new_sum not in dp_sums and new_subset != other_subset:
                            dp_sums.add(new_sum)

    return sorted(list(dp_sums))

nums = list(map(int, input().split()))
print(*find_distinct_sums(nums), sep=' ')
