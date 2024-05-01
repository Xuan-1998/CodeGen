from functools import lru_cache

def distinct_sums(nums):
    @lru_cache(None)
    def subset_sum(i, memo):
        if i == 0:  # base case: empty subset
            return set()
        sums = set()
        for j in range(i + 1):
            new_sum = nums[j] + (subset_sum(i - 1, memo)[-1] if i > 1 else 0)
            if new_sum not in memo:
                memo[new_sum] = True
                sums.add(new_sum)
        return sums

    return ' '.join(map(str, sorted(set(subset_sum(len(nums), {})))))

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    print(distinct_sums(nums))
