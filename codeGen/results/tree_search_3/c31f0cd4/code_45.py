from functools import lru_cache

def distinct_sums(nums):
    @lru_cache(None)
    def subset_sum(subset):
        return sum(subset)

    @lru_cache(None)
    def powerset(index, subset):
        if index == 0:
            return [(subset, subset_sum(subset))]
        prev_powersets = powerset(0, tuple())
        result = []
        for prev_subset in prev_powersets:
            new_subset = prev_subset[1] + (nums[index],)
            result.append((new_subset, subset_sum(new_subset)))
            if len(prev_subset[0]) > 0:
                new_subset = prev_subset[0]
                result.append((new_subset, subset_sum(new_subset)))
        return result

    numsets = powerset(len(nums), tuple())
    distinct_sums = set()
    for _, total in numsets:
        distinct_sums.add(total)
    return ' '.join(map(str, sorted(distinct_sums)))

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(distinct_sums(nums))
